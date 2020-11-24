from rest_framework import generics, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema

from .models import Log
from .serializers import LogSerializer

class LogsFilterView(generics.ListAPIView):
    """
    Pesquisa logs pelos campos 'title', 'description',
    'level' e 'origin' passando o parâmetro '?search='

    * É preciso estar autenticado para pesquisar.
    """
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'description', 'level', 'origin']

class LogListCreateView(generics.ListCreateAPIView):
    
    serializer_class = LogSerializer

    @swagger_auto_schema(responses={
        200: LogSerializer(many=True),
        401: 'Você não possui credenciais de autenticação válidas',
    })
    def get(self, request):
        """
        Lista todos os logs

        * É preciso estar autenticado para visualizar.
        """
        queryset = Log.objects.all()
        serializer = LogSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={
        201: LogSerializer(),
        401: 'Você não possui credenciais de autenticação válidas',
        400: 'Má formatação',
    }, request_body=LogSerializer)
    def post(self, request):
        """
        Cria um novo log
        
        * É preciso estar autenticado para visualizar.
        """
        log = request.data
        serializer = LogSerializer(data=log)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class LogDetailView(APIView):

    serializer_class = LogSerializer

    @swagger_auto_schema(responses={
        200: LogSerializer(),
        401: 'Você não possui credenciais de autenticação válidas',
        404: 'Não encontrado',
    })
    def get(self, request, pk):
        """
        Lista detalhes de um log

        * É preciso estar autenticado para visualizar.
        """
        queryset = get_object_or_404(Log, pk=pk)
        serializer = LogSerializer(queryset)
        return Response(serializer.data)

    @swagger_auto_schema(responses={
        202: LogSerializer(),
        400: 'Má formatação',
        401: 'Você não possui credenciais de autenticação válidas',
        404: 'Não encontrado',
    }, request_body=LogSerializer)
    def put(self, request, pk):
        """
        Altera todos os dados do log

        * É preciso estar autenticado para editar.
        """
        queryset = get_object_or_404(Log, pk=pk)
        serializer = LogSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={
        202: LogSerializer(),
        400: 'Má formatação',
        401: 'Você não possui credenciais de autenticação válidas',
        404: 'Não encontrado',
    }, request_body=LogSerializer)
    def patch(self, request, pk):
        """
        Altera parcialmente o log

        * É preciso estar autenticado para editar.
        """
        queryset = get_object_or_404(Log, pk=pk)
        serializer = LogSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={
        204: 'Sem conteúdo',
        401: 'Você não possui credenciais de autenticação válidas',
        404: 'Não encontrado'
    })
    def delete(self, request, pk):
        """
        Deleta um log

        * É preciso estar autenticado para deletar.
        """
        queryset = get_object_or_404(Log, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    