from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.HomeViewSet)

urlpatterns = [
    path('authentication', include('authentication.urls')),
]

urlpatterns += router.urls