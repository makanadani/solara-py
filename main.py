'''
SOLARA

GRUPO
EcoMinds

INTEGRANTES
Adonay Rodrigues da Rocha | RM 558782
Marina Yumi Kanadani | RM 558404
Pedro Henrique Martins dos Reis | RM 555306
'''

from fastapi import FastAPI, HTTPException
from app.crud import projetos

app = FastAPI()


# Rotas para Projetos Sustentáveis
@app.get("/projetos")
def listar_projetos():
    try:
        return projetos.exibir_todos_projetos()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar projetos: {e}")


@app.get("/projetos/{id}")
def listar_projeto_por_id(id: int):
    try:
        projeto = projetos.exibir_projeto_por_id(id)
        if not projeto:
            raise HTTPException(status_code=404, detail="Projeto não encontrado")
        return projeto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar projeto: {e}")


@app.post("/projetos")
def criar_projeto(dados: dict):
    try:
        return projetos.inserir_projeto(dados)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar projeto: {e}")


@app.put("/projetos/{id}")
def atualizar_projeto(id: int, dados: dict):
    try:
        return projetos.alterar_projeto(id, dados)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar projeto: {e}")


@app.delete("/projetos/{id}")
def deletar_projeto(id: int):
    try:
        return projetos.excluir_projeto(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir projeto: {e}")
