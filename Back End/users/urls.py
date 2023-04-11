# from rest_framework import routers
# from users.views import UserModelViewSet, UserViewSet
#
# r = routers.DefaultRouter()
# r.register(r'', UserModelViewSet)
# r.register(r'create', UserViewSet)
#
# urlpatterns = r.urls
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.UserViewSet.as_view({'post': 'create_user'}))
]
