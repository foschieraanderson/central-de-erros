from rest_framework import viewsets

from .models import Log
from .serializers import LogSerializer

class HomeViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer 