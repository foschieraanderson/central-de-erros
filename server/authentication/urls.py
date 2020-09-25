from django.urls import path
from authentication import views
from .custom_token_response import MyTokenObtainPairView, MyTokenRefreshView


app_name = 'authentication'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),

    # rotas protegidas somente para usuários registrados
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),

    # rotas protegidas para super usuários (is_staff=True, is_superuser=True)
    path('users/', views.ListUsersView.as_view(), name='all_users'),
    path('users/<int:pk>', views.SingleUserView.as_view(), name='single_user')
]