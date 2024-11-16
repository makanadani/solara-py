'''
SOLARA

GRUPO
EcoMinds

INTEGRANTES
Adonay Rodrigues da Rocha | RM 558782
Marina Yumi Kanadani | RM 558404
Pedro Henrique Martins dos Reis | RM 555306
'''

from app import validations, connection

# Auxiliar - Exibir Regiões Disponíveis
def exibir_regioes_disponiveis():
    print("""
    |========= REGIÕES DISPONÍVEIS ==========|
    | [1] Norte                              |
    | [2] Sul                                |
    | [3] Leste                              |
    | [4] Oeste                              |
    | [5] Centro-Oeste                       |
    |========================================|
    """)

# CREATE - Inserir Região Sustentável
def inserir_regiao():
    try:
        exibir_regioes_disponiveis()
        nome_regiao = validations.validar_texto("Digite o nome da nova região sustentável")
        if nome_regiao is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            INSERT INTO tb_regioes_sustentaveis (nome_regiao)
            VALUES (:1)
        """, [nome_regiao])
        connection.conn.commit()
        print(f"Região '{nome_regiao}' inserida com sucesso!")
        cursor.close()
    except Exception as e:
        print("Erro ao inserir a região:", e)

# READ - Exibir Região Sustentável por ID
def exibir_regiao_por_id():
    try:
        id_regiao = validations.validar_numero("Digite o ID da Região Sustentável")
        if id_regiao is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_regiao, nome_regiao
            FROM tb_regioes_sustentaveis
            WHERE id_regiao = :1
        """, [id_regiao])
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            print(f"ID: {resultado[0]}, Nome: {resultado[1]}")
        else:
            print("Nenhuma região encontrada com o ID informado.")
    except Exception as e:
        print("Erro ao buscar a região:", e)

# READ - Exibir Todas as Regiões Sustentáveis
def exibir_todas_regioes():
    try:
        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_regiao, nome_regiao
            FROM tb_regioes_sustentaveis
            ORDER BY id_regiao ASC
        """)
        resultados = cursor.fetchall()
        cursor.close()

        if resultados:
            print("| ID | Nome da Região |")
            for row in resultados:
                print(f"| {row[0]} | {row[1]} |")
        else:
            print("Nenhuma região sustentável cadastrada.")
    except Exception as e:
        print("Erro ao buscar as regiões sustentáveis:", e)

# UPDATE - Alterar Região Sustentável
def alterar_regiao():
    try:
        id_regiao = validations.validar_numero("Digite o ID da Região Sustentável que deseja alterar")
        if id_regiao is None:
            return

        novo_nome = validations.validar_texto("Digite o novo nome da região sustentável")
        if novo_nome is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            UPDATE tb_regioes_sustentaveis
            SET nome_regiao = :1
            WHERE id_regiao = :2
        """, (novo_nome, id_regiao))
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Região sustentável alterada com sucesso!")
        else:
            print("Nenhuma região encontrada com o ID informado.")
        cursor.close()
    except Exception as e:
        print("Erro ao alterar a região:", e)

# DELETE - Excluir Região Sustentável
def excluir_regiao():
    try:
        id_regiao = validations.validar_numero("Digite o ID da Região Sustentável que deseja excluir")
        if id_regiao is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            DELETE FROM tb_regioes_sustentaveis
            WHERE id_regiao = :1
        """, [id_regiao])
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Região sustentável excluída com sucesso!")
        else:
            print("Nenhuma região encontrada com o ID informado.")
        cursor.close()
    except Exception as e:
        print("Erro ao excluir a região:", e)
