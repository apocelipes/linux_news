from django.db import models


class NewsTag(models.Model):
    """新闻类型
    """
    tag_name = models.CharField(max_length=50)
    origin = models.ForeignKey('NewsOrigin', on_delete=models.CASCADE)

    def __str__(self):
        return f'tag_name: {self.tag_name} origin: {self.origin.origin_name}'
