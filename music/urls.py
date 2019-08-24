from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [

    path('about/', views.About, name='about'),

    # /music/
    path('', views.IndexView.as_view(), name='index'),

    # /music/<album_id>
    path('album/<pk>', views.DetailView.as_view(), name='detail'),

    # /music/album/add
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/delete
    path('album/<pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/album/update
    path('album/<pk>/update/', views.AlbumUpdate.as_view(), name='album-update'),

    path('song/create/', views.SongCreate.as_view(), name='song-create'),
    path('song/all/', views.SongList.as_view(), name='song-list'),
    path('song/<id>/', views.SongDetail, name='song-detail'),

]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
