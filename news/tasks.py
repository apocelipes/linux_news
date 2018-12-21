from linux_news.celery import app
from celery import shared_task
from .models import *
from django.db.models import Q
from datetime import datetime
from .feedsfilter import filters
import time
import feedparser
import pytz
import html


@app.task(ignore_result=True)
def fetch_news(origin_name):
    """
    fetch all news from origin_name
    :param origin_name: fetch news from origin_name
    """
    origin = NewsOrigin.objects.get(origin_name=origin_name)
    feeds = feedparser.parse(origin.feed_link)
    for item in feeds['entries']:
        condition = Q(link=item.link) & Q(origin__origin_name=origin.origin_name)
        if NewsEntry.objects.filter(condition).exists():
            continue

        entry = NewsEntry()
        entry.title = item.title
        entry.origin = origin
        entry.author = item.author
        entry.link = item.link
        entry.publish_time = structtime_2_datetime(item.published_parsed)
        # parse后的struct_time已经是utc时间
        entry.publish_time = entry.publish_time.replace(tzinfo=pytz.utc)

        summary_filter = filters.get(origin.origin_name)
        if summary_filter is None:
            # summary has some HTML tag, we need escape them
            entry.summary = html.escape(item.summary)
        else:
            entry.summary = html.escape(summary_filter(item.title, item.summary))

        entry.save()

        # add tags
        for t in item.tags:
            name = t['term']
            condition = Q(tag_name=name) & Q(origin__origin_name=origin.origin_name)
            tag = NewsTag.objects.filter(condition).first()
            if tag is None:
                tag = NewsTag()
                tag.tag_name = name
                tag.origin = origin
                tag.save()

            entry.tags.add(tag)


def structtime_2_datetime(t):
    """
    convert struct_time to datetime
    :param t: time.struct_time
    :return: datetime
    """
    return datetime.fromtimestamp(time.mktime(t))


@shared_task
def fetch_all_news():
    """
    fetch all origins' news to db
    """
    origins = NewsOrigin.objects.all()
    for origin in origins:
        fetch_news.delay(origin.origin_name)
