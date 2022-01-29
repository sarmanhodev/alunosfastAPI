from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


app = FastAPI() 

class Aluno(BaseModel):
    id: int =0
    nome: str
    email:str


banco_de_dados=[
    Aluno(id=1, nome="Fulano",email="fulano@fulano.com"),
    Aluno(id=2, nome="Ciclano",email="ciclano@ciclano.com"),
    Aluno(id=3, nome="Beltrano",email="beltrano@beltrano.com"),
]


@app.get("/")
async def read(): 
    """
    Mensagem de boas vindas!
    """
    return {"Bem-vindo a FastAPI!"}


@app.get("/alunos/")
async def lista_todos_alunos():
    """
    Retorna todos arquivos existentes na variável banco_de_dados
    """
    return banco_de_dados


@app.get("/alunos/id/{aluno_id}")
async def lista_alunos_id(aluno_id:int):
    """
    Realiza a busca pelo id de um determinado dado cadastrado na variável banco_de_dados
    """
    return {"aluno": [alunos for alunos in banco_de_dados if alunos.id == aluno_id]}


@app.get("/alunos/nome/{nome}")
async def nomes(nome:str):
    """
    Realiza a busca pelo nome de um determinado dado cadastrado na variável banco_de_dados
    """
    return [alunos for alunos in banco_de_dados if alunos.nome.upper() == nome.upper()]


@app.post("/alunos")
async def cadastra(aluno: Aluno):
    """
    Cria um novo registro na variável banco_de_dados
    """
    try:
        aluno.id = banco_de_dados[-1].id+1
        banco_de_dados.append(aluno)
        time = datetime.now()
        data = time.strftime("%d/%m/%Y %H:%M")
        #prints retornam registro e data e hora do registro no terminal
        print("\nNovo registro inserido com sucesso: {} \n".format(aluno))
        print("Dados registrados em {}\n".format(data))

        return {"Sucess"}
    except Exception as e:
        return {"Error", 404}


@app.patch("/alunos/id/{aluno_id}")
async def update(aluno_id: int, aluno:Aluno):
    """
    Atualiza um registro da variável banco_de_dados
    """
    index = [index for index, aluno in enumerate (banco_de_dados) if aluno.id == aluno_id]
    aluno.id= banco_de_dados[index[0]].id
    banco_de_dados[index[0]] = aluno
    return {"Cadastro atualizado!"}


@app.delete("/alunos/id/{aluno_id}")
async def delete(aluno_id:int):
    """
    Deleta um registro da variável banco_de_dados
    """
    aluno = [ aluno for aluno in banco_de_dados if aluno.id == aluno_id]
    banco_de_dados.remove(aluno[0])
    return {"Registro apagado"}
