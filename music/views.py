from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album, Song
from django.shortcuts import render, redirect, get_object_or_404


def About(request):
    return render(request, 'music/about.html', {})


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
    template_name = 'music/album_confirm_delete.html'


class SongCreate(CreateView):
    model = Song
    fields = ['album', 'files', 'song_title']
    success_url = reverse_lazy('music:index')
    template_name = 'music/song_create.html'


class SongList(generic.ListView):
    template_name = 'music/song_list.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.all()


class SongDelete(DeleteView):
    model = Song
    #success_url = reverse_lazy('music:song-list')
    template_name = 'music/song_delete.html'

    def get_queryset(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Song, id=id_)


def SongDetail(request, id):
    songs = get_object_or_404(Song, id=id)

    if request.method == "POST":
        songs.delete()
        return redirect('/')

    template_name = 'music/song_detail.html'
    context = {"all_songs": songs}

    return render(request, template_name, context)
