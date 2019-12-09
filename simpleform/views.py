from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This will be list of all albums</h1>")


def detail(request, album_id):
    return HttpResponse("<h2>Detail for album id: " + str(album_id)+"</h3>")
