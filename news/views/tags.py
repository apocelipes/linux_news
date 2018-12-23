from rest_framework.generics import ListAPIView
from django.http import Http404
from ..models import NewsTag
from ..serializers import NewsTagSerializer


class GetOriginTags(ListAPIView):
    """
    get all tags of the origin
    """
    lookup_field = "origin_name"
    serializer_class = NewsTagSerializer

    def get_queryset(self):
        origin_name = self.kwargs.get(self.lookup_field)
        if origin_name is None:
            raise Http404

        return NewsTag.objects.filter(origin__origin_name=origin_name)
