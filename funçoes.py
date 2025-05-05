import json
import os

CAMINHO_ARQUIVO = "usuario.json"

def carregar_usuarios():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return {}
    with open(CAMINHO_ARQUIVO, 'r') as arquivo:
        return json.load(arquivo)
    
def salvar_usuarios(usuarios):
    with open(CAMINHO_ARQUIVO, "w") as arquivo:
         json.dump(usuarios, arquivo, indent=4)

def cadastrar():
    email = input('Digite seu email: ').strip()
    senha = input('Digite sua senha: ').strip()

    usuarios = carregar_usuarios()

    if email in usuarios:
        print('Esse email ja está cadastrado')
    else:
        usuarios[email] = senha
        salvar_usuarios(usuarios)
        print('Cadastro realizado com sucesso!')

def login():
    email = input('Digite seu email: ').strip()
    senha = input('Digite sua senha: ').strip()

    usuarios = carregar_usuarios()

    if usuarios.get(email) == senha:
        print('login bem sucedido! Seja bem vindo')
    else:
        print('Email ou senha invalido')

def menu():
    while True:
        print('Sistema de Login')
        print('1 Cadastrar')
        print('2 fazer login')
        print('3 sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            login()
        elif opcao == '3':
            print('saindo...')
            break
        else:
            print('opcao invalida')