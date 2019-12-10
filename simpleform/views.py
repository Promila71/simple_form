from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    html = ""
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2>Detail for album id: " + str(album_id)+"</h3>")
