from django.urls import path

from .custom_token import MyObtainJSONWebToken, MyRefreshJSONWebToken

from . import views

app_name = 'authentication'

urlpatterns = [
    # Endpoint para registro de usuários
    path('register/', views.RegisterView.as_view(), name='register'),

    # Endpoints protegidas para usuários registrados 
    path('token/', MyObtainJSONWebToken.as_view(), name='obtain_token'),
    path('token/refresh/', MyRefreshJSONWebToken.as_view(), name='refresh_token'),

    # Endpoints protegidas para super usuários 
    path('users/', views.UserListView.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]