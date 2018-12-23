from django.urls import path
from .views import tags


urlpatterns = [
    path('tags/<str:origin_name>/', tags.GetOriginTags.as_view(), name='get_origin_name'),
]
