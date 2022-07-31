from django.shortcuts import render


def videos(request, slug):
    video = {'titulo': 'Video: Apresentação', 'vimeo_id': 251224475}
    return render(request, 'videos/video.html', context={'video': video})
