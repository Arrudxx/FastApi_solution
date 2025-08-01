from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context

auth_router = APIRouter(prefix='/auth', tags=['Auth'])

@auth_router.get('/')
async def home():
    """
    Essa é a rota padrão de autenticação do nosso sistema.
    """
    return {'mensagem': 'Você acessou a rota padrão de autenticação', 'autenticado':False}

@auth_router.post('/criar_conta')
async def criar_conta(email: str, senha:str, nome: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        #Já existe um usuario com este email
        return HTTPException(status_code= 400, detail="E-mail de usuário já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {'mensagem': f'usuario cadastrado com sucesso: {email}'}