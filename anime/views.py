from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

from .models import Anime

# Create your views here.
@login_required
def index(request):
    anime_list = Anime.objects.all()
    context = {
        'anime_list': anime_list,
    }
    return render(request, 'anime/index.html', context)


def detail(request, title):
    try:
        anime = Anime.objects.get(title=title)
    except Anime.DoesNotExist:
        raise Http404("そのアニメは存在しません...")

    stories = anime.story_set.order_by('id')

    context = {
        'anime': anime,
        'stories': stories,
    }
    return render(request, 'anime/detail.html', context)
