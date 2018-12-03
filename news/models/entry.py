from django.db import models


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

    class Meta:
        ordering = ['-publish_time']
