from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist      = models.CharField(max_length=150)
    album_title = models.CharField(max_length=100)
    genre       = models.CharField(max_length=100)
    logo        = models.ImageField(upload_to="images/", blank=True, null=True)

    def get_absolute_url(self):
        return reverse(viewname='music:detail', kwargs={'pk': self.pk})
        
    def update_absolute_url(self):
        return reverse(viewname='music:album-update', kwargs={'pk': self.pk})

    def delete_absolute_url(self):
        return reverse(viewname='music:album-delete', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + " by " + self.artist


class Song(models.Model):
    album       = models.ForeignKey(Album, on_delete=models.CASCADE)
    files       = models.FileField(upload_to='musics/', null=True)
    song_title  = models.CharField(max_length=200)

    def __str__(self):
        return str(self.files) + ' - ' + str(self.id)

    def delete_song_absolute_url(self):
        return reverse(viewname='music:song-detail', kwargs={'id': self.id})
