from django.urls import include, path
from .views import  ArtisteList, ArtisteDetails, SongList, SongDetails , LyricList, LyricDetails

urlpatterns = [
    path("song/<int:pk>/", SongDetails.as_view(), name="song_Lyric"),
    path("song/", SongList.as_view(), name="song_list"),
    path("artiste/<int:pk>/", ArtisteDetails.as_view(), name="artiste_Songs"),
    path("artiste/", ArtisteList.as_view(), name="artiste_List"),
    path("lyric/", LyricList.as_view(), name="Lyric"),
    path("lyric/<int:pk>/", LyricDetails.as_view(), name="lyric_Details"),
    # path('', include(.urls))
]