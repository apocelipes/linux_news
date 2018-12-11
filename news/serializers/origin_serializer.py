from rest_framework import serializers
from ..models import NewsOrigin


class NewsOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsOrigin
        fields = ('origin_name', 'feed_link')
