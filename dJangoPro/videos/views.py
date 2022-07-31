from django.shortcuts import render


def videos(request, slug):
    videos = {
        'apresentacao':{'titulo': 'Video: Apresentação', 'vimeo_id': 251224475},
        'instalacao-windows': {'titulo': 'Video: Instalacao Windows', 'vimeo_id': 251497668}
    }
    video = videos[slug]
    return render(request, 'videos/video.html', context={'video': video})
