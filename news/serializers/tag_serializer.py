from rest_framework import serializers
from ..models import NewsTag


class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTag
        fields = ('tag_name',)
