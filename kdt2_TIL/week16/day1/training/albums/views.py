from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album


# Create your views here.
def index(request):    
    albums = Album.objects.all()
    form = AlbumForm()
    
    context = {
        'albums': albums,
        'form': form,
    }
    return render(request, 'albums/index.html', context)


def redirect_index(_):
    return redirect('albums:index')


def create(request):
    if request.method == 'POST':
        form = AlbumForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            
    return redirect_index(request)


def delete(_, album_pk):
    album = Album.objects.get(pk=album_pk)
    album.delete()
    return redirect('albums:index')


def update(request, album_pk):
    album = Album.objects.get(pk=album_pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, files=request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect_index(request)
        
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'albums/update.html', context)