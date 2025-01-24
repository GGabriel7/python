import os
dir = os.path.dirname(os.path.abspath(__file__))
dbPath = os.path.join(dir, 'tarefas.db')

from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(f'sqlite:///{dbPath}')
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    tarefas = relationship("Tarefa", back_populates="usuario")

class Tarefa(Base):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True)
    descricao = Column(String, nullable=False)
    concluida = Column(Boolean, default=False)
    usuarioId = Column(Integer, ForeignKey('usuarios.id'))

    usuario = relationship("Usuario", back_populates="tarefas")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print("Banco de dados configurado com sucesso!")


def adicionarUsuario(nome, email):
    novoUsuario = Usuario(nome=nome, email=email)
    session.add(novoUsuario)
    session.commit()
    print(f"Usuário '{nome}' adicionado com sucesso!")


def adicionarTarefa(descricao, usuarioId):
    novaTarefa = Tarefa(descricao=descricao, usuarioId=usuarioId)
    session.add(novaTarefa)
    session.commit()
    print(f"Tarefa '{descricao}' adicionada para o usuário {usuarioId}!")


def listarTarefas(usuarioId):
    usuario = session.query(Usuario).filter_by(id=usuarioId).first()

    if usuario:
        print(f"Tarefas do usuário '{usuario.nome}':")
        for tarefa in usuario.tarefas:
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"ID da Tarefa: {tarefa.id} | {tarefa.descricao} | Status: {status}")

    else:
        print("Usuário não encontrado.")


def concluirTarefa(tarefaId):
    tarefa = session.query(Tarefa).filter_by(id=tarefaId).first()

    if tarefa:
        tarefa.concluida = True
        session.commit()
        print(f"Tarefa '{tarefa.descricao}' marcada como concluída!")
    
    else:
        print("Tarefa não encontrada.")


def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Tarefas ===")
        print("1. Adicionar Usuário")
        print("2. Adicionar Tarefa")
        print("3. Listar Tarefas de um Usuário")
        print("4. Concluir Tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            adicionarUsuario(nome, email)

        elif escolha == "2":
            descricao = input("Descrição da Tarefa: ")
            usuarioId = int(input("ID do usuário: "))
            adicionarTarefa(descricao, usuarioId)

        elif escolha == "3":
            id = int(input("ID do usuário: "))
            listarTarefas(id)

        elif escolha == "4":
            id = int(input("ID da tarefa: "))
            concluirTarefa(id)

        elif escolha == "5":
            print("Saindo do sistema...")
            break

        else:
            ("Opção inválida! Tente novamente.")


menu()