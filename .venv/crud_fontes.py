'''
SOLARA

GRUPO
EcoMinds

INTEGRANTES
Adonay Rodrigues da Rocha | RM 558782
Marina Yumi Kanadani | RM 558404
Pedro Henrique Martins dos Reis | RM 555306
'''

import connection
import validations

# CREATE - Inserir Tipo de Fonte
def inserir_tipo_fonte():
    try:
        nome_fonte = validations.validar_texto("Digite o nome do tipo de fonte de energia")
        if nome_fonte is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            INSERT INTO tb_tipo_fontes (nome_fonte) 
            VALUES (:1)
        """, [nome_fonte])
        connection.conn.commit()
        print(f"Tipo de fonte '{nome_fonte}' inserido com sucesso!")
        cursor.close()
    except Exception as e:
        print("Erro ao inserir o tipo de fonte:", e)


# READ - Exibir Tipo de Fonte por ID
def exibir_tipo_fonte_por_id():
    try:
        id_tipo_fonte = validations.validar_numero("Digite o ID do Tipo de Fonte de Energia")
        if id_tipo_fonte is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_tipo_fonte, nome_fonte
            FROM tb_tipo_fontes
            WHERE id_tipo_fonte = :1
        """, [id_tipo_fonte])
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            print(f"ID: {resultado[0]}, Nome: {resultado[1]}")
        else:
            print("Nenhum tipo de fonte encontrado com o ID informado.")
    except Exception as e:
        print("Erro ao buscar o tipo de fonte:", e)


# READ - Exibir Todos os Tipos de Fontes
def exibir_todos_tipos_fontes():
    try:
        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_tipo_fonte, nome_fonte
            FROM tb_tipo_fontes
            ORDER BY id_tipo_fonte ASC
        """)
        resultados = cursor.fetchall()
        cursor.close()

        if resultados:
            print("| ID | Nome do Tipo de Fonte            |")
            print("|----|----------------------------------|")
            for row in resultados:
                print(f"| {row[0]:<2} | {row[1]:<32} |")
        else:
            print("Nenhum tipo de fonte de energia cadastrado.")
    except Exception as e:
        print("Erro ao buscar os tipos de fontes:", e)


# UPDATE - Alterar Tipo de Fonte
def alterar_tipo_fonte():
    try:
        id_tipo_fonte = validations.validar_numero("Digite o ID do Tipo de Fonte de Energia que deseja alterar")
        if id_tipo_fonte is None:
            return

        novo_nome = validations.validar_texto("Digite o novo nome do tipo de fonte de energia")
        if novo_nome is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            UPDATE tb_tipo_fontes
            SET nome_fonte = :1
            WHERE id_tipo_fonte = :2
        """, (novo_nome, id_tipo_fonte))
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Tipo de fonte alterado com sucesso!")
        else:
            print("Nenhum tipo de fonte encontrado com o ID informado.")
        cursor.close()
    except Exception as e:
        print("Erro ao alterar o tipo de fonte:", e)


# DELETE - Excluir Tipo de Fonte
def excluir_tipo_fonte():
    try:
        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_tipo_fonte, nome_fonte
            FROM tb_tipo_fontes
        """)
        tipos_fontes = cursor.fetchall()

        if not tipos_fontes:
            print("Nenhum tipo de fonte cadastrado para excluir.")
            return

        print("| ID | Nome do Tipo de Fonte  |")
        for tipo in tipos_fontes:
            print(f"| {tipo[0]:<2} | {tipo[1]:<22} |")

        id_tipo_fonte = validations.validar_numero("Digite o ID do Tipo de Fonte de Energia que deseja excluir")
        if id_tipo_fonte is None:
            return

        cursor.execute("""
            DELETE FROM tb_tipo_fontes
            WHERE id_tipo_fonte = :1
        """, [id_tipo_fonte])
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Tipo de fonte excluído com sucesso!")
        else:
            print("Nenhum tipo de fonte encontrado com o ID informado.")
        cursor.close()
    except Exception as e:
        print("Erro ao excluir o tipo de fonte:", e)
2