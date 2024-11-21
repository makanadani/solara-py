'''
SOLARA

GRUPO
EcoMinds

INTEGRANTES
Adonay Rodrigues da Rocha | RM 558782
Marina Yumi Kanadani | RM 558404
Pedro Henrique Martins dos Reis | RM 555306
'''
import json

import pandas as pd

import queries
# Importar as funções CRUD
from crud.comunidades import *
from crud.emissoes import *
from crud.empresas import *
from crud.fontes import *
from crud.medicoes import *
from crud.projetos import *
from crud.regioes import *
from crud.sensores import *


# Exportar resultados
def exportar_resultados(dados, colunas, nome_base):
    print("Como deseja exportar os resultados?")
    print("[1] JSON")
    print("[2] Excel")
    escolha = input("Escolha o formato de exportação: ").strip()
    if escolha == "1":
        nome_arquivo = f"{nome_base}.json"
        with open(nome_arquivo, 'w') as arquivo_json:
            json.dump([dict(zip(colunas, linha)) for linha in dados], arquivo_json, indent=4)
        print(f"Dados exportados para {nome_arquivo}")
    elif escolha == "2":
        nome_arquivo = f"{nome_base}.xlsx"
        df = pd.DataFrame(dados, columns=colunas)
        df.to_excel(nome_arquivo, index=False, engine='openpyxl')
        print(f"Dados exportados para {nome_arquivo}")
    else:
        print("Opção inválida! Nenhum arquivo foi exportado.")

# Menu de consultas
def menu_consultas():
    while True:
        print("""
        |=========== MENU DE CONSULTAS ===========|
        | [1] Consultar comunidades por região   |
        | [2] Consultar projetos por status      |
        | [3] Consultar sensores por comunidade  |
        | [4] Voltar ao menu principal           |
        |========================================|
        """)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            queries.consultar_comunidades_por_regiao()
        elif opcao == "2":
            queries.consultar_projetos_por_status()
        elif opcao == "3":
            queries.consultar_sensores_por_comunidade()
        elif opcao == "4":
            break
        else:
            print("Opção inválida! Tente novamente.")


# Menus individuais
def menu_fontes():
    while True:
        print("""
        |============ FONTES DE ENERGIA ============|
        | [1] Inserir Tipo de Fonte                |
        | [2] Exibir Fonte por ID                  |
        | [3] Exibir Todas as Fontes               |
        | [4] Alterar Tipo de Fonte                |
        | [5] Excluir Tipo de Fonte                |
        | [6] Voltar                               |
        |==========================================|
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            inserir_tipo_fonte()
        elif escolha == "2":
            exibir_tipo_fonte_por_id()
        elif escolha == "3":
            exibir_todos_tipos_fontes()
        elif escolha == "4":
            alterar_tipo_fonte()
        elif escolha == "5":
            excluir_tipo_fonte()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")


def menu_projetos():
    while True:
        print("""
        |========== PROJETOS SUSTENTÁVEIS =========|
        | [1] Inserir Projeto                      |
        | [2] Exibir Projeto por ID                |
        | [3] Exibir Todos os Projetos             |
        | [4] Alterar Projeto                      |
        | [5] Excluir Projeto                      |
        | [6] Voltar                               |
        |==========================================|
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            inserir_projeto()
        elif escolha == "2":
            exibir_projeto_por_id()
        elif escolha == "3":
            exibir_todos_projetos()
        elif escolha == "4":
            alterar_projeto()
        elif escolha == "5":
            excluir_projeto()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")


def menu_emissoes():
    while True:
        print("""
        |========== EMISSÕES DE CARBONO ==========|
        | [1] Inserir Emissão                     |
        | [2] Exibir Emissão por ID               |
        | [3] Exibir Todas as Emissões            |
        | [4] Alterar Emissão                     |
        | [5] Excluir Emissão                     |
        | [6] Voltar                              |
        |=========================================|
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            inserir_emissao()
        elif escolha == "2":
            exibir_emissao_por_id()
        elif escolha == "3":
            exibir_todas_emissoes()
        elif escolha == "4":
            alterar_emissao()
        elif escolha == "5":
            excluir_emissao()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")


def menu_regioes():
    while True:
        print("""
        |========== REGIÕES SUSTENTÁVEIS =========|
        | [1] Inserir Região                      |
        | [2] Exibir Região por ID                |
        | [3] Exibir Todas as Regiões             |
        | [4] Alterar Região                      |
        | [5] Excluir Região                      |
        | [6] Voltar                              |
        |=========================================|
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            inserir_regiao()
        elif escolha == "2":
            exibir_regiao_por_id()
        elif escolha == "3":
            exibir_todas_regioes()
        elif escolha == "4":
            alterar_regiao()
        elif escolha == "5":
            excluir_regiao()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")


def menu_sensores():
    while True:
        print("""
        |============= SENSORES IoT ==============|
        | [1] Inserir Sensor                      |
        | [2] Exibir Sensor por ID                |
        | [3] Exibir Todos os Sensores            |
        | [4] Alterar Sensor                      |
        | [5] Excluir Sensor                      |
        | [6] Voltar                              |
        |=========================================|
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            inserir_sensor()
        elif escolha == "2":
            exibir_sensor_por_id()
        elif escolha == "3":
            exibir_todos_sensores()
        elif escolha == "4":
            alterar_sensor()
        elif escolha == "5":
            excluir_sensor()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")


def menu_medicoes():
    while True:
        print("""
        |=============== MEDIÇÕES ===============|
        | [1] Inserir Medição                    |
        | [2] Exibir Medição por ID              |
        | [3] Exibir Todas as Medições           |
        | [4] Alterar Medição                    |
        | [5] Excluir Medição                    |
        | [6] Voltar                             |
        |========================================|
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            inserir_medicao()
        elif escolha == "2":
            exibir_medicao_por_id()
        elif escolha == "3":
            exibir_todas_medicoes()
        elif escolha == "4":
            alterar_medicao()
        elif escolha == "5":
            excluir_medicao()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")


def menu_comunidades():
    while True:
        print("""
        |============ COMUNIDADES ==============|
        | [1] Inserir Comunidade                |
        | [2] Exibir Comunidade por ID          |
        | [3] Exibir Todas as Comunidades       |
        | [4] Alterar Comunidade                |
        | [5] Excluir Comunidade                |
        | [6] Voltar                            |
        |=======================================|
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            inserir_comunidade()
        elif escolha == "2":
            exibir_comunidade_por_id()
        elif escolha == "3":
            exibir_todas_comunidades()
        elif escolha == "4":
            alterar_comunidade()
        elif escolha == "5":
            excluir_comunidade()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")


def menu_empresas():
    while True:
        print("""
        |============== EMPRESAS ===============|
        | [1] Inserir Empresa                   |
        | [2] Exibir Empresa por ID             |
        | [3] Exibir Todas as Empresas          |
        | [4] Alterar Empresa                   |
        | [5] Excluir Empresa                   |
        | [6] Voltar                            |
        |=======================================|
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            inserir_empresa()
        elif escolha == "2":
            exibir_empresa_por_id()
        elif escolha == "3":
            exibir_todas_empresas()
        elif escolha == "4":
            alterar_empresa()
        elif escolha == "5":
            excluir_empresa()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")

# Menu principal
def menu_principal():
    while True:
        print("""
        |================= MENU =====================|
        | [1] Fontes de Energia                      |
        | [2] Projetos Sustentáveis                  |
        | [3] Emissões de Carbono                    |
        | [4] Regiões Sustentáveis                   |
        | [5] Sensores IoT                           |
        | [6] Medições                               |
        | [7] Comunidades                            |
        | [8] Empresas                               |
        | [9] Consultas                              |
        | [10] Sair                                  |
        |============================================|   
        """)
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            menu_fontes()
        elif escolha == "2":
            menu_projetos()
        elif escolha == "3":
            menu_emissoes()
        elif escolha == "4":
            menu_regioes()
        elif escolha == "5":
            menu_sensores()
        elif escolha == "6":
            menu_medicoes()
        elif escolha == "7":
            menu_comunidades()
        elif escolha == "8":
            menu_empresas()
        elif escolha == "9":
            menu_consultas()
        elif escolha == "10":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

