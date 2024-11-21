from app.script.popula_comunidades import inserir_comunidades
from app.script.popula_comunidades_projetos import gerar_comunidades_projetos, inserir_comunidades_projetos
from app.script.popula_empresas import inserir_empresas, empresas_reais
from app.script.popula_medicoes import inserir_medicoes
from app.script.popula_sensores import inserir_sensores


def popula_tudo():
    etapas = {
        "Empresas": lambda: inserir_empresas(empresas_reais),
        "Comunidades": lambda: inserir_comunidades(),
        "Sensores IoT": lambda: inserir_sensores(),
        "Medições": lambda: inserir_medicoes(),
        "Comunidades e Projetos": lambda: popula_comunidades_projetos(),
    }

    resultados = {}

    print("\n--- Iniciando o preenchimento automático ---\n")

    for nome, funcao in etapas.items():
        try:
            print(f"Populando tabela de {nome.lower()}...")
            funcao()
            print(f"Tabela de {nome.lower()} populada com sucesso.")
            resultados[nome] = "Sucesso"
        except Exception as e:
            print(f"Erro ao popular tabela de {nome.lower()}: {e}")
            resultados[nome] = f"Erro: {e}"

    print("\n--- Resumo do preenchimento ---")
    for etapa, resultado in resultados.items():
        print(f"{etapa}: {resultado}")

    print("\nProcesso de preenchimento concluído.")


def popula_comunidades_projetos():
    """
    Combina as funções de geração e inserção de associações entre comunidades e projetos.
    """
    comunidades_projetos = gerar_comunidades_projetos()
    if comunidades_projetos:
        inserir_comunidades_projetos(comunidades_projetos)
    else:
        print("Nenhuma associação entre comunidades e projetos foi gerada.")


if __name__ == "__main__":
    popula_tudo()
