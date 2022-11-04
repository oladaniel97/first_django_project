from django.shortcuts import render
from rest_framework import generics
from .models import Artiste , Song , Lyric
from .serializers import ArtisteSerializers, SongSerializers , LyricSerializers


# Create your views here.
class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializers

class ArtisteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializers

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializers

class SongDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializers

class LyricList(generics.ListCreateAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializers

class LyricDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializers