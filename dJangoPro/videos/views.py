from django.shortcuts import render


def videos(request, slug):
    return render(request, 'videos/video.html')
