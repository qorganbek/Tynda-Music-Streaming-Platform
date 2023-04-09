from rest_framework import routers
from users.views import UserModelViewSet

r = routers.DefaultRouter()
r.register(r'users', UserModelViewSet)

urlpatterns = r.urls
