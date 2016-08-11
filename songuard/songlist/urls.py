from django.conf.urls import url

from . import views
# http://tutorial.djangogirls.org/en/django_views/
# The simplest view can look like this:
# def post_list(request):
#     return render(request, 'blog/post_list.html', {})
#
#


#anything past base url is passed to this list

urlpatterns = [
    # if nothing passed base url, returns index(list of recent songs)
    #caret means beginning, dollar means end.
    url(r'^$', views.index, name='index'),
    # if /1 returns that song "You're looking at song 2."
    url(r'^(?P<song_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^mackie/', views.mackie, name='mackie'),
    url(r'^song/(?P<song_id>[0-9]+)/$', views.song, name='song')

]
