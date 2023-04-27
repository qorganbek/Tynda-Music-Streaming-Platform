from django.urls import path, include
from accounts import views

urlpatterns = [
    path('accounts/create/', views.UserViewSet.as_view({'post': 'create_user'})),
]
