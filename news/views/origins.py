from rest_framework.generics import ListAPIView
from ..models import NewsOrigin
from ..serializers import NewsOriginSerializer


class GetAllOrigins(ListAPIView):
    queryset = NewsOrigin.objects.all()
    serializer_class = NewsOriginSerializer
