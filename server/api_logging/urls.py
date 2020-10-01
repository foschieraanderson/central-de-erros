from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="API Central de Erros",
      default_version='1.0',
      description="API para centralização de logs de erro",
      terms_of_service="https://github.com/foschieraanderson/central-de-erros",
      contact=openapi.Contact(email="foschieraanderson@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # App Admin
    path('admin/', admin.site.urls),
    # Endpoints de authenticação e usuários
    path('api/v1/auth/', include('authentication.urls')),
    # Endpoints de logs
    path('api/v1/logs/', include('logs.urls')),

    #Documentação
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]