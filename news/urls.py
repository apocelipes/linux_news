from django.urls import path
from .views import tags, origins


urlpatterns = [
    path('tags/<str:origin_name>/', tags.GetOriginTags.as_view(), name='get_origin_name'),
    path('origins/', origins.GetAllOrigins.as_view(), name="get_all_origins"),
]
