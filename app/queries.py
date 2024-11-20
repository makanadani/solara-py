from app.connection import conecta_banco
from app.menu import *

# Consulta 1: Comunidades por região
def consultar_comunidades_por_regiao():
    regiao = input("Digite o nome da região: ").strip()
    conn = conecta_banco()
    if conn:
        cursor = conn.cursor()
        query = """
            SELECT c.nome_comunidade, c.latitude_comunidade, c.longitude_comunidade, r.nome_regiao
            FROM tb_comunidades c
            JOIN tb_regioes_sustentaveis r ON c.id_regiao = r.id_regiao
            WHERE r.nome_regiao = :1
        """
        cursor.execute(query, [regiao])
        resultados = cursor.fetchall()
        colunas = ["Nome da Comunidade", "Latitude", "Longitude", "Região"]
        conn.close()
        if resultados:
            exportar_resultados(resultados, colunas, "comunidades_por_regiao")
        else:
            print("Nenhum resultado encontrado.")

# Consulta 2: Projetos por status
def consultar_projetos_por_status():
    status = input("Digite o status do projeto (Em andamento ou Concluído): ").strip()
    conn = conecta_banco()
    if conn:
        cursor = conn.cursor()
        query = """
            SELECT p.descricao_projeto, p.custo_projeto, p.status_projeto
            FROM tb_projetos_sustentaveis p
            WHERE p.status_projeto = :1
        """
        cursor.execute(query, [status])
        resultados = cursor.fetchall()
        colunas = ["Descrição do Projeto", "Custo", "Status"]
        conn.close()
        if resultados:
            exportar_resultados(resultados, colunas, "projetos_por_status")
        else:
            print("Nenhum resultado encontrado.")

# Consulta 3: Sensores por comunidade
def consultar_sensores_por_comunidade():
    comunidade = input("Digite o nome da comunidade: ").strip()
    conn = conecta_banco()
    if conn:
        cursor = conn.cursor()
        query = """
            SELECT s.id_sensor, s.tipo_sensor, s.descricao_sensaor, c.nome_comunidade
            FROM tb_sensores s
            JOIN tb_comunidades c ON s.id_comunidade = c.id_comunidade
            WHERE c.nome_comunidade LIKE :1
        """
        cursor.execute(query, [f"%{comunidade}%"])
        resultados = cursor.fetchall()
        colunas = ["ID do Sensor", "Tipo do Sensor", "Descrição", "Comunidade"]
        conn.close()
        if resultados:
            exportar_resultados(resultados, colunas, "sensores_por_comunidade")
        else:
            print("Nenhum resultado encontrado.")

def exportar_resultados(dados, colunas, nome_base):
    """
    :param dados: Resultados da consulta (lista de tuplas).
    :param colunas: Nomes das colunas dos resultados.
    :param nome_base: Nome base para o arquivo de saída.
    """


    print("Escolha um formato para exportar:")
    print("[1] JSON")
    print("[2] Excel")
    escolha = input("Escolha uma opção: ").strip()

    if escolha == "1":
        nome_arquivo = f"{nome_base}.json"
        with open(nome_arquivo, 'w') as arquivo_json:
            json.dump([dict(zip(colunas, linha)) for linha in dados], arquivo_json, indent=4)
        print(f"Data exported to {nome_arquivo}")
    elif escolha == "2":
        nome_arquivo = f"{nome_base}.xlsx"
        df = pd.DataFrame(dados, columns=colunas)
        df.to_excel(nome_arquivo, index=False, engine='openpyxl')
        print(f"Dados exportados para {nome_arquivo}")
    else:
        print("Opção inválida. Nenhum arquivo foi exportado.")
