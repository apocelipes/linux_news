from linux_news.celery import app
from celery import shared_task
from .models import *
from django.db.models import Q
from datetime import datetime
import time
import feedparser


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
        entry.summary = item.summary
        entry.save()

        # add tags
        for t in item.tags:
            tag = NewsTag()
            tag.tag_name = t['term']
            tag.origin = origin
            tag.save()
            entry.tags.add(tag)

        #entry.save()


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
