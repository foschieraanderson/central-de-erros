from .serializers import UserSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    """
    Sobrescrevendo a view padrão de autenticação do JWT e
    adicionando dados do usuário na resposta
    """
    return {
        'token': token,
        'user': UserSerializer(user, context={'request':request}).data
    }