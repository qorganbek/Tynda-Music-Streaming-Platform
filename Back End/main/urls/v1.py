from django.urls import path
from rest_framework import routers
from main import views

r = routers.DefaultRouter()

r.register(r'songs', views.SongModelViewSet)

r.register(r'categories', views.CategoryModelViewSet)

r.register(r'artists', views.ArtistModelViewSet)

r.register(r'favorite', views.FavoriteModelViewSet)

r.register(r'playlist', views.PlaylistModelViewSet)

r.register(r'library', views.LibraryModelViewSet)

urlpatterns = [
    path('songs/create/', views.SongViewSet.as_view({'post': 'create_song'})),
    path('songs/verify/', views.SongViewSet.as_view({'post': 'verify_song'})),
]

urlpatterns += r.urls


