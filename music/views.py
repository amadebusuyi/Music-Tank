from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album, Song
from .forms import AlbumForm, SongForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = "albums"

    def get_queryset(self):
    	return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = "music/details.html"

class AlbumCreate(CreateView):
	model = Album
	form_class = AlbumForm

class AlbumUpdate(UpdateView):
	model = Album
	form_class = AlbumForm

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy("music:index")


class SongCreate(CreateView, generic.DetailView):
	model = Album
	form_class = SongForm
	template_name = "music/song_form.html"

class SongUpdate(UpdateView, generic.DetailView):
	model = Album
	form_class = SongForm
	template_name = "music/song_form.html"

class SongDelete(DeleteView):
	model = Album
	form_class = SongForm
	success_url = reverse_lazy("music:index")

		
def back(request):
	return render(request, "music/index.html")

def songs(request):
	return render(request, "music/songs.html", {'songs': Song.objects.all()})

def songDetail(request, id):
	return render(request, "music/song_detail.html", {'song': Song.objects.get(pk = id)})

# from music.models import Album, Song
# album = Album.objects.get(pk = 1)
# album.song_set.create(song_title = "Hello world", file_type = "mp3")


def favorite(request, id):
	album = Album.objects.get(pk = id)
	try:
		song = album.song_set.get(pk = request.GET['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, "music/details.html", {
			"error_message": "The requested song does not exist",
			"album": album
			})
	else:
		if song.is_favorite == True:
			song.is_favorite = False
		else:
			song.is_favorite = True

		song.save()
		return render(request, "music/details.html", {"album": album})
