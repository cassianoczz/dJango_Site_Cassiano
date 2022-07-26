from django.urls import path
from dJangoPro.videos.views import video

app_name = 'videos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
