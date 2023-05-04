from django.urls import path, include
from accounts import views

urlpatterns = [
    path('users/create/', views.UserViewSet.as_view({'post': 'create_user'})),
]
