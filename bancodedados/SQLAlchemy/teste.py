from time import sleep

import os
dir = os.path.dirname(os.path.abspath(__file__))
dbPath = os.path.join(dir, 'arquivoTeste.db')

from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(f'sqlite:///{dbPath}')
Base = declarative_base()

class Tabela(Base):
    __tablename__ = 'tabela'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print("Banco de dados configurado com sucesso!")


def adicionarPessoa(nome, idade):
    novoUsuario = Tabela(nome=nome, idade=idade)
    session.add(novoUsuario)
    session.commit()
    print(f"Usuário '{nome}' adicionado com sucesso!")


def listarUsuarios():
    usuarios = session.query(Tabela).all()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario.id} | {usuario.nome} | Idade: {usuario.idade}")
    
    else:
        print("Usuário não encontrado.")


def alterarNome(id, novoNome):
    usuario = session.query(Tabela).filter_by(id=id).first()
    if usuario:
        usuario.nome = novoNome
        session.commit()
        print("Nome alterado!")
    
    else:
        print(f"Usuário com ID {id} não encontrado.")


def alterarIdade(id, novaIdade):
    usuario = session.query(Tabela).filter_by(id=id).first()
    if usuario:
        usuario.idade = novaIdade
        session.commit()
        print("Idade alterada!")
    
    else:
        print(f"Usuário com ID {id} não encontrado.")


def deletar(id):
    usuario = session.query(Tabela).filter_by(id=id).first()
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f"Usuário '{usuario.nome}' deletado com sucesso.")
    
    else:
        print(f"Usuário com ID {id} não encontrado.")



def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Pessoas ===\n")
        print("1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Alterar Nome")
        print("4. Alterar Idade")
        print("5. Deletar Usuário")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            adicionarPessoa(nome, idade)

        elif escolha == "2":
            listarUsuarios()
            sleep(2)

        elif escolha == "3":
            id = int(input("Informe o ID do usuário: "))
            novoNome = input("Informe o novo nome: ")
            alterarNome(id, novoNome)

        elif escolha == "4":
            id = int(input("Informe o ID do usuário: "))
            novaIdade = input("Informe a nova idade: ")
            alterarIdade(id, novaIdade)
        
        elif escolha == "5":
            id = int(input("Informe o ID do usuário a ser deletado: "))
            deletar(id)

        elif escolha == "6":
            print("Saindo do sistema. Até logo!")
            sleep(2)
            session.close()
            break

        else: print("Opção inválida. Tente novamente.")


menu()