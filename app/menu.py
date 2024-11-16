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
from app.crud import sensores, empresas, projetos, fontes, regioes, emissoes, medicoes, comunidades

# Função genérica para exibir menus e chamar CRUDs
def exibir_menu(titulo, opcoes, crud_module):
    while True:
        print(f"\n|============ {titulo.upper()} ============|")
        for i, opcao in enumerate(opcoes, start=1):
            print(f"| [{i}] {opcao} {' ' * (40 - len(opcao))}|")
        print("| [6] Voltar                               |")
        print("|==========================================|")

        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            crud_module.inserir()
        elif escolha == "2":
            crud_module.exibir_por_id()
        elif escolha == "3":
            crud_module.exibir_todos()
        elif escolha == "4":
            crud_module.alterar()
        elif escolha == "5":
            crud_module.excluir()
        elif escolha == "6":
            break
        else:
            print("Opção inválida!")


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
            exibir_menu("Fontes de Energia",
                        ["Inserir Tipo de Fonte", "Exibir Fonte por ID", "Exibir Todas", "Alterar Tipo de Fonte",
                         "Excluir Tipo de Fonte"],
                        fontes)
        elif escolha == "2":
            exibir_menu("Projetos Sustentáveis",
                        ["Inserir Projeto", "Exibir Projeto por ID", "Exibir Todos", "Alterar Projeto",
                         "Excluir Projeto"],
                        projetos)
        elif escolha == "3":
            exibir_menu("Emissões de Carbono",
                        ["Inserir Emissão", "Exibir Emissão por ID", "Exibir Todas", "Alterar Emissão",
                         "Excluir Emissão"],
                        emissoes)
        elif escolha == "4":
            exibir_menu("Regiões Sustentáveis",
                        ["Inserir Região", "Exibir Região por ID", "Exibir Todas", "Alterar Região", "Excluir Região"],
                        regioes)
        elif escolha == "5":
            exibir_menu("Sensores IoT",
                        ["Inserir Sensor", "Exibir Sensor por ID", "Exibir Todos", "Alterar Sensor", "Excluir Sensor"],
                        sensores)
        elif escolha == "6":
            exibir_menu("Medições",
                        ["Inserir Medição", "Exibir Medição por ID", "Exibir Todas", "Alterar Medição",
                         "Excluir Medição"],
                        medicoes)
        elif escolha == "7":
            exibir_menu("Comunidades",
                        ["Inserir Comunidade", "Exibir Comunidade por ID", "Exibir Todas", "Alterar Comunidade",
                         "Excluir Comunidade"],
                        comunidades)
        elif escolha == "8":
            exibir_menu("Empresas",
                        ["Inserir Empresa", "Exibir Empresa por ID", "Exibir Todas", "Alterar Empresa",
                         "Excluir Empresa"],
                        empresas)
        elif escolha == "9":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 9.")
