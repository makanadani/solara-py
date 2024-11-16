'''
SOLARA

GRUPO
EcoMinds

INTEGRANTES
Adonay Rodrigues da Rocha | RM 558782
Marina Yumi Kanadani | RM 558404
Pedro Henrique Martins dos Reis | RM 555306
'''


def validar_numero(mensagem, tipo="int", permitir_vazio=False, mensagem_erro="Entrada inválida."):
    """
    Valida uma entrada numérica do usuário.
    """
    while True:
        entrada = input(f"{mensagem} (ou 'V' para voltar): ").strip()
        if entrada.upper() == "V":
            print("Voltando ao menu anterior...")
            return None
        if permitir_vazio and not entrada:
            return None
        try:
            if tipo == "int":
                return int(entrada)
            elif tipo == "float":
                return float(entrada)
        except ValueError:
            print(mensagem_erro)


def validar_texto(mensagem, permitir_vazio=False, mensagem_erro="O texto não pode estar vazio."):
    """
    Valida uma entrada de texto do usuário.
    """
    while True:
        entrada = input(f"{mensagem} (ou 'V' para voltar): ").strip()
        if entrada.upper() == "V":
            print("Voltando ao menu anterior...")
            return None
        if permitir_vazio or entrada:
            return entrada
        print(mensagem_erro)


def validar_opcao(mensagem, opcoes, mensagem_erro="Opção inválida."):
    """
    Valida uma entrada do usuário contra uma lista de opções permitidas.
    """
    while True:
        entrada = input(f"{mensagem} (ou 'V' para voltar): ").strip()
        if entrada.upper() == "V":
            print("Voltando ao menu anterior...")
            return None
        if entrada in opcoes:
            return entrada
        print(f"{mensagem_erro} Opções válidas: {', '.join(opcoes)}.")


def validar_id_existente(mensagem, ids_validos, mensagem_erro="ID inválido."):
    """
    Valida se um ID informado pelo usuário existe em uma lista de IDs válidos.
    """
    while True:
        entrada = validar_numero(mensagem, tipo="int")
        if entrada is None or entrada in ids_validos:
            return entrada
        print(mensagem_erro)
