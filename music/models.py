from django.db import models
from django.urls import reverse

# Create your models here.

# # # # # # # # # # # # # # # # # # # # #
# To update or create database			#
# 	1. makemigrations [app_name]		#
# 	2. migrate							#
# # # # # # # # # # # # # # # # # # # # #

class Album(models.Model):
	artist = models.CharField(max_length = 250)
	album_title = models.CharField(max_length = 500)
	genre = models.CharField(max_length = 200)
	album_logo = models.CharField(max_length = 1000)

	def get_absolute_url(self):
		return reverse('music:detail', kwargs = {'pk': self.pk})

	def __str__(self):
		return self.album_title +" (Genre: "+ self.genre + ") - "+self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	file_type = models.CharField(max_length = 250)
	song_title = models.CharField(max_length = 250)
	is_favorite = models.BooleanField(default = False)


	def get_absolute_url(self):
		return reverse('music:song_detail', kwargs = {'id': self.pk})

	def __str__(self):
		return self.song_title+" (Album: "+self.album.album_title+")"