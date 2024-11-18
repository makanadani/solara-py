"""
SOLARA

GRUPO
EcoMinds

INTEGRANTES
Adonay Rodrigues da Rocha | RM 558782
Marina Yumi Kanadani | RM 558404
Pedro Henrique Martins dos Reis | RM 555306
"""

from fastapi import FastAPI
from app.routes import router  # Importando as rotas da API
from app.menu import menu_principal  # Importando o menu principal
import uvicorn

# Criando a aplicação FastAPI
app = FastAPI(
    title="Solara API",
    description="API para gerenciamento de dados do projeto Solara",
    version="1.0.0"
)

# Registrar as rotas da API
app.include_router(router, prefix="/api")

# Rota raiz
@app.get("/")
async def root():
    return {"message": "Bem-vindo à API Solara!"}

# Função para rodar o servidor FastAPI
def run_api():
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    """
    Ponto de entrada do sistema.
    Executa o menu principal ou inicia o servidor da API.
    """
    print("Bem-vindo ao sistema SOLARA")
    print("Selecione uma das opções abaixo:")
    print("1 - Iniciar API")
    print("2 - Executar menu principal")

    escolha = input("Digite sua escolha (1 ou 2): ")

    if escolha == "1":
        print("Iniciando o servidor da API...")
        run_api()
    elif escolha == "2":
        print("Executando o menu principal...")
        menu_principal()
    else:
        print("Opção inválida. Encerrando o programa.")
