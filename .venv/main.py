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
import menu

# Função principal para execução do programa
def main():
    try:
        while True:
            # Exibe o menu principal
            menu.menu_principal()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido manualmente. Até logo!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
