from django import forms
from .models import Album, Song


class AlbumForm(forms.ModelForm):

    class Meta:
    	model = Album
    	fields = ['artist', 'album_title', 'genre', 'album_logo']
    	widgets = {
    	'artist': forms.TextInput(
    		attrs= {
    		'class': 'form-control'
    		}
    		),
    	'album_title': forms.TextInput(
    		attrs= {
    		'class': 'form-control'
    		}
    		),
    	'genre': forms.TextInput(
    		attrs= {
    		'class': 'form-control'
    		}
    		),
    	'album_logo': forms.TextInput(
    		attrs = {
    		'class': 'form-control'
    		}
    		)
    	}


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['file_type', 'song_title', 'album']
        widgets = {
        'file_type': forms.TextInput(
            attrs= {
            'class': 'form-control'
            }
            ),
        'song_title': forms.TextInput(
            attrs= {
            'class': 'form-control'
            }
            )
        }
