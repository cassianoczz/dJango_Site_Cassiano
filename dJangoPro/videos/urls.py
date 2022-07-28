from django.urls import path
from dJangoPro.videos.views import videos

app_name = 'videos'
urlpatterns = [
    path('<slug:slug>', videos, name='videos'),
]
