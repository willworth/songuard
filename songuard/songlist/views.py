from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#The dot before models means current directory or current application
from .models import Song


def index(request):
    latest_song_list = Song.objects.order_by('-pub_date')[:5]
    context = {'latest_song_list': latest_song_list}
    return render(request, 'songlist/index.html', context)

def mackie(request):
    return HttpResponse ("The mackie test view works.")


def detail(request, song_id):
    return HttpResponse("You're looking at song %s." % song_id)

def song(request, song_id):

    num = song_id
    song = Song.objects.get(pk=num)
    return render(request, 'songlist/song.html', {'song': song})
