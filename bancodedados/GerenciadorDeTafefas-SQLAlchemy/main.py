from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///tarefas.db')
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
    novoUsuario = Usuario(nome=nome, emial=email)
    session.add(novoUsuario)
    print(f"Usuário '{nome}' adicionado com sucesso!")