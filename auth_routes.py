from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['Auth'])

@auth_router.get('/')
async def authenticate():
    """
    Essa é a rota padrão de autenticação do nosso sistema.
    """

    return {'mensagem': 'Você acessou a rota padrão de autenticação', 'autenticado':False}

