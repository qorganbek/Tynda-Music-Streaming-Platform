from rest_framework import routers
from . import views

r = routers.DefaultRouter()
r.register(r'songs', views.SongModelViewSet)
r.register(r'categories', views.CategoryModelViewSet)
r.register(r'artists', views.ArtistModelViewSet)
r.register(r'favorite', views.FavoriteModelViewSet)
urlpatterns = r.urls