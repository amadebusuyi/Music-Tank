from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
	#./music
    path('', views.IndexView.as_view(), name = "index"),

    #./music/<id>
    path('<pk>/', views.DetailView.as_view(), name = "detail"),

    #To make a song favorite ./music/<id>/favorite
    path('<id>/favorite', views.favorite, name = "favorite"),

    #./music/album/create to add new album
    path('album/add/', views.AlbumCreate.as_view(), name = "create_album"),

    #./music/album/<pk> to add new album
    path('album/<pk>/', views.AlbumUpdate.as_view(), name = "update_album"),

    #./music/album/<pk>/delete to add new album
    path('album/<pk>/delete', views.AlbumDelete.as_view(), name = "delete_album"),

    #./music/songs/list to get list of all songs
    path('songs/list', views.songs, name = "songs"),

    #./music/songs/list/<id> to view a single song details
    path('album/song/list/<id>/', views.songDetail, name = "song_detail"),

    #./music/song/add/<pk>
    path('album/song/add/<pk>', views.SongCreate.as_view(), name = "add-song"),

    #./music/song/<pk>
    path('album/song/<pk>/', views.SongUpdate.as_view(), name = "update-song"),

    #./music/song/<pk>/delete
    path('album/song/<pk>/delete', views.SongDelete.as_view(), name = "delete-song"),

    # to navigate to the previous page
    path('../', views.back, name = "back"),
]
