from django.urls import path

from . import views

app_name = 'logs'

urlpatterns = [
    # Endpoints protegidas somente para usuários registrados
    path('logs/', views.LogListCreateView.as_view(), name='logs-list'),
    path('logs/<int:pk>', views.LogDetailView.as_view(), name='log-detail'),
    path('logs/filters', views.LogsFilterView.as_view(), name='logs-filter'),
]