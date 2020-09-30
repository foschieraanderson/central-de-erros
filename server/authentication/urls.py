from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views

app_name = 'authentication'

urlpatterns = [
    # Endpoint para registro de usuários
    path('register/', views.RegisterView.as_view(), name='register'),

    # Endpoints protegidas para usuários registrados 
    path('token/', obtain_jwt_token, name='obtain_token'),
    path('token/refresh/', refresh_jwt_token, name='refresh_token'),

    # Endpoints protegidas para super usuários 
    path('users/', views.ListUsersView.as_view(), name='users-list'),
    path('users/<int:pk>/', views.DetailUserView.as_view(), name='user-detail'),
]