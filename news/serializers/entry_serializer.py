from rest_framework import serializers
from ..models import NewsEntry


class NewsEntrySerializer(serializers.ModelSerializer):
    origin_name = serializers.CharField(source='origin.origin_name', max_length=50)
    tags_info = serializers.SerializerMethodField()

    def get_tags_info(self, entry):
        tags = entry.tags.all()
        ret = []
        for tag in tags:
            ret.append({
                'tag_name': tag.tag_name,
            })

        return ret

    class Meta:
        model = NewsEntry
        fields = ('origin_name',
                  'tags_info',
                  'title',
                  'author',
                  'publish_time',
                  'summary',
                  'link',
                  )
