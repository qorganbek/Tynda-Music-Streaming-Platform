from django.urls import path
from rest_framework import routers
from . import views


r = routers.DefaultRouter()
r.register(r'audio', views.AudioViewSet)


urlpatterns = r.urls