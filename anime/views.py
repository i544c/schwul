from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

from .models import Anime

# Create your views here.
@login_required
def index(request):
    anime_list = Anime.objects.all()
    context = {
        'anime_list': anime_list,
    }
    return render(request, 'anime/index.html', context)


def add(request):
    if request.POST:
        title = request.POST['title']
        bc_year = request.POST['bc_year']
        synopsis = request.POST['synopsis']
        if title and bc_year and synopsis:
            anime = Anime(title=title, bc_year=bc_year, synopsis=synopsis)
            anime.save()
            return render(request, 'anime/add.html', {
                'message': "追加"
            })

    return render(request, 'anime/add.html')


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


def edit(request, title):
    try:
        anime = Anime.objects.get(title=title)
    except Anime.DoesNotExist:
        raise Http404("そのアニメは存在しません...")

    context = {
        'anime': anime,
    }

    return render(request, 'anime/edit.html', context)
