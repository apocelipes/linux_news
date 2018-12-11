from django.db import models
from ..utils import as_local_timezone


class NewsEntry(models.Model):
    """存储新闻信息
    """
    origin = models.ForeignKey('NewsOrigin', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_time = models.DateTimeField()
    summary = models.TextField()
    link = models.URLField(unique=True)
    tags = models.ManyToManyField('NewsTag')

    def __str__(self):
        pub_time = as_local_timezone(self.publish_time)
        return f'origin: {self.origin.origin_name} ' +\
               f'title: {self.title} author: {self.author} ' +\
               f'publish_time: {pub_time.strftime("%Y/%m/%d %H:%M:%S")} ' +\
               f'link: {self.link}'

    class Meta:
        ordering = ['-publish_time']
