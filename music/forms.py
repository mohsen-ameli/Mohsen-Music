from django import forms
from .models import Song


class SongCreateForm(forms.Form):
    album      = Forms.CharField() 
    song_title = Forms.CharField() 

    class Meta:
        model = Song

        fields = ['album', 'files', 'song_title']
