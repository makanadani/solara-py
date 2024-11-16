'''
SOLARA

GRUPO
EcoMinds

INTEGRANTES
Adonay Rodrigues da Rocha | RM 558782
Marina Yumi Kanadani | RM 558404
Pedro Henrique Martins dos Reis | RM 555306
'''

# Importando módulos
import crud_projetos
import crud_regioes
import crud_emissoes
import crud_fontes
import crud_sensores
import crud_medicoes
import crud_comunidades
import crud_empresas

# Menu Principal
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
        | [9] Sair                                   |
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
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 9.")

# Submenus
def menu_fontes():
    while True:
        print("""
        |=========== FONTES DE ENERGIA ==============|
        | [1] Inserir Tipo de Fonte de Energia       |
        | [2] Exibir Tipo de Fonte de Energia por ID |
        | [3] Exibir Todas as Fontes de Energia      |
        | [4] Alterar Tipo de Fonte de Energia       |
        | [5] Excluir Tipo de Fonte de Energia       |    
        | [6] Voltar                                 |
        |============================================|   
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            crud_fontes.inserir_tipo_fonte()
        elif escolha == "2":
            crud_fontes.exibir_tipo_fonte_por_id()
        elif escolha == "3":
            crud_fontes.exibir_todos_tipos_fontes()
        elif escolha == "4":
            crud_fontes.alterar_tipo_fonte()
        elif escolha == "5":
            crud_fontes.excluir_tipo_fonte()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")

def menu_projetos():
    while True:
        print("""
        |========= PROJETOS SUSTENTÁVEIS ============|
        | [1] Inserir Projeto Sustentável            |
        | [2] Exibir Projeto Sustentável por ID      |
        | [3] Exibir Todos os Projetos Sustentáveis  |
        | [4] Alterar Projeto Sustentável            |
        | [5] Excluir Projeto Sustentável            |    
        | [6] Voltar                                 |
        |============================================|   
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            crud_projetos.inserir_projeto()
        elif escolha == "2":
            crud_projetos.exibir_projeto_por_id()
        elif escolha == "3":
            crud_projetos.exibir_todos_projetos()
        elif escolha == "4":
            crud_projetos.alterar_projeto()
        elif escolha == "5":
            crud_projetos.excluir_projeto()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")

def menu_emissoes():
    while True:
        print("""
        |========== EMISSÕES DE CARBONO ============|
        | [1] Inserir Emissão de Carbono             |
        | [2] Exibir Emissão de Carbono por ID       |
        | [3] Exibir Todas as Emissões de Carbono    |
        | [4] Alterar Emissão de Carbono             |
        | [5] Excluir Emissão de Carbono             |    
        | [6] Voltar                                 |
        |============================================|   
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            crud_emissoes.inserir_emissao()
        elif escolha == "2":
            crud_emissoes.exibir_emissao_por_id()
        elif escolha == "3":
            crud_emissoes.exibir_todas_emissoes()
        elif escolha == "4":
            crud_emissoes.alterar_emissao()
        elif escolha == "5":
            crud_emissoes.excluir_emissao()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")

def menu_regioes():
    while True:
        print("""
        |========== REGIÕES SUSTENTÁVEIS ============|
        | [1] Inserir Região Sustentável             |
        | [2] Exibir Região Sustentável por ID       |
        | [3] Exibir Todas as Regiões Sustentáveis   |
        | [4] Alterar Região Sustentável             |
        | [5] Excluir Região Sustentável             |    
        | [6] Voltar                                 |
        |============================================|   
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            crud_regioes.inserir_regiao()
        elif escolha == "2":
            crud_regioes.exibir_regiao_por_id()
        elif escolha == "3":
            crud_regioes.exibir_todas_regioes()
        elif escolha == "4":
            crud_regioes.alterar_regiao()
        elif escolha == "5":
            crud_regioes.excluir_regiao()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")

def menu_sensores():
    while True:
        print("""
        |============ SENSORES IOT =================|
        | [1] Inserir Sensor                        |
        | [2] Exibir Sensor por ID                  |
        | [3] Exibir Todos os Sensores              |
        | [4] Alterar Sensor                        |
        | [5] Excluir Sensor                        |    
        | [6] Voltar                                |
        |===========================================|   
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            crud_sensores.inserir_sensor()
        elif escolha == "2":
            crud_sensores.exibir_sensor_por_id()
        elif escolha == "3":
            crud_sensores.exibir_todos_sensores()
        elif escolha == "4":
            crud_sensores.alterar_sensor()
        elif escolha == "5":
            crud_sensores.excluir_sensor()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")

def menu_medicoes():
    while True:
        print("""
        |============== MEDIÇÕES ==================|
        | [1] Inserir Medição                      |
        | [2] Exibir Medição por ID                |
        | [3] Exibir Todas as Mediçõe              |
        | [4] Alterar Medição                      |
        | [5] Excluir Medição                      |    
        | [6] Voltar                               |
        |==========================================|   
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            crud_medicoes.inserir_medicao()
        elif escolha == "2":
            crud_medicoes.exibir_medicao_por_id()
        elif escolha == "3":
            crud_medicoes.exibir_todas_medicoes()
        elif escolha == "4":
            crud_medicoes.alterar_medicao()
        elif escolha == "5":
            crud_medicoes.excluir_medicao()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")

def menu_comunidades():
    while True:
        print("""
        |============= COMUNIDADES ================|
        | [1] Inserir Comunidade                   |
        | [2] Exibir Comunidade por ID             |
        | [3] Exibir Todas as Comunidades          |
        | [4] Alterar Comunidade                   |
        | [5] Excluir Comunidade                   |    
        | [6] Voltar                               |
        |==========================================|   
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            crud_comunidades.inserir_comunidade()
        elif escolha == "2":
            crud_comunidades.exibir_comunidade_por_id()
        elif escolha == "3":
            crud_comunidades.exibir_todas_comunidades()
        elif escolha == "4":
            crud_comunidades.alterar_comunidade()
        elif escolha == "5":
            crud_comunidades.excluir_comunidade()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")

def menu_empresas():
    while True:
        print("""
        |=============== EMPRESAS =================|
        | [1] Inserir Empresa                      |
        | [2] Exibir Empresa por ID                |
        | [3] Exibir Todas as Empresas             |
        | [4] Alterar Empresa                      |
        | [5] Excluir Empresa                      |    
        | [6] Voltar                               |
        |==========================================|   
        """)
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            crud_empresas.inserir_empresa()
        elif escolha == "2":
            crud_empresas.exibir_empresa_por_id()
        elif escolha == "3":
            crud_empresas.exibir_todas_empresas()
        elif escolha == "4":
            crud_empresas.alterar_empresa()
        elif escolha == "5":
            crud_empresas.excluir_empresa()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")
