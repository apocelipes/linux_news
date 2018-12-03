from django.db import models


class NewsOrigin(models.Model):
    """保存新闻站点和其rss link。
    """
    origin_name = models.CharField(max_length=50, unique=True)
    feed_link = models.URLField()

    def __str__(self):
        return f'origin_name: {self.origin_name}\nlink: {self.feed_link}'
