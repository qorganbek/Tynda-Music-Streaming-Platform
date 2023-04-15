from rest_framework import routers
from main import views

r = routers.DefaultRouter()

r.register(r'songs', views.SongModelViewSet)

r.register(r'categories', views.CategoryModelViewSet)

r.register(r'artists', views.ArtistModelViewSet)

r.register(r'favorite', views.FavoriteModelViewSet)

r.register(r'playlist', views.PlaylistModelViewSet)

urlpatterns = r.urls
