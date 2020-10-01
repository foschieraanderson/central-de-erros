from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

class MyObtainJSONWebToken(ObtainJSONWebToken):
    """
    Gera um token válido a partir do e-mail e senha de um usuário registrado

    * Retorna um JSON Web Token que pode ser usado para solicitações autenticadas.
    """

class MyRefreshJSONWebToken(RefreshJSONWebToken):
    """
    Atualiza o token de acesso

    * Retorna um JSON Web Token atualizado com base no token existente.
    """