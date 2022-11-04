from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from .models import Artiste, Song, Lyric

class ArtisteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ('first_name','last_name','age')

class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('artiste_id','title', 'date_released', 'likes')

class LyricSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lyric
        fields = ('song_id','content')