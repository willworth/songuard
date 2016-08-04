from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Song


def index(request):
    latest_song_list = Song.objects.order_by('-pub_date')[:5]
    context = {'latest_song_list': latest_song_list}
    return render(request, 'songlist/index.html', context)




def detail(request, song_id):
    return HttpResponse("You're looking at song %s." % song_id)
