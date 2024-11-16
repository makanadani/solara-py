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

# CREATE - Inserir Emissão de Carbono
def inserir_emissao():
    try:
        # Exibir tipos de fontes disponíveis
        cursor = connection.conn.cursor()
        cursor.execute("SELECT id_tipo_fonte, nome_fonte FROM tb_tipo_fontes")
        tipos_fontes = cursor.fetchall()

        if not tipos_fontes:
            print("Nenhum tipo de fonte disponível. Cadastre um tipo de fonte antes.")
            return

        print("| ID  | Nome do Tipo de Fonte |")
        for fonte in tipos_fontes:
            print(f"| {fonte[0]:<4} | {fonte[1]:<20} |")

        id_tipo_fonte = validations.validar_id_existente(
            "Digite o ID do tipo de fonte associado", [fonte[0] for fonte in tipos_fontes]
        )
        if id_tipo_fonte is None:
            return

        emissao = validations.validar_numero("Digite o valor da emissão de carbono (em toneladas)", tipo="float")
        if emissao is None or emissao <= 0:
            print("O valor da emissão deve ser maior que zero.")
            return

        # Inserir no banco
        cursor.execute("""
            INSERT INTO tb_emissoes_carbono (id_tipo_fonte, emissao)
            VALUES (:1, :2)
        """, [id_tipo_fonte, emissao])
        connection.conn.commit()
        print("Emissão de carbono inserida com sucesso!")
        cursor.close()

    except Exception as e:
        print("Erro ao inserir emissão de carbono:", e)

# READ - Exibir Emissão de Carbono por ID
def exibir_emissao_por_id():
    try:
        id_emissao = validations.validar_numero("Digite o ID da emissão de carbono que deseja consultar")
        if id_emissao is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_emissao, id_tipo_fonte, emissao
            FROM tb_emissoes_carbono
            WHERE id_emissao = :1
        """, [id_emissao])
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            print(f"ID Emissão: {resultado[0]}, Tipo de Fonte ID: {resultado[1]}, Valor da Emissão: {resultado[2]:.2f}")
        else:
            print("Nenhuma emissão encontrada com o ID informado.")

    except Exception as e:
        print("Erro ao consultar emissão de carbono:", e)

# READ - Exibir Todas as Emissões de Carbono
def exibir_todas_emissoes():
    try:
        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_emissao, id_tipo_fonte, emissao
            FROM tb_emissoes_carbono
            ORDER BY id_emissao ASC
        """)
        resultados = cursor.fetchall()
        cursor.close()

        if resultados:
            print("| ID  | Tipo de Fonte ID | Valor da Emissão (ton) |")
            print("|-----|------------------|-----------------------|")
            for row in resultados:
                print(f"| {row[0]:<4} | {row[1]:<16} | {row[2]:<21.2f} |")
        else:
            print("Nenhuma emissão de carbono cadastrada.")

    except Exception as e:
        print("Erro ao listar todas as emissões de carbono:", e)

# UPDATE - Alterar Emissão de Carbono
def alterar_emissao():
    try:
        id_emissao = validations.validar_numero("Digite o ID da emissão de carbono que deseja alterar")
        if id_emissao is None:
            return

        # Verificar se o ID existe
        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_emissao, emissao
            FROM tb_emissoes_carbono
            WHERE id_emissao = :1
        """, [id_emissao])
        resultado = cursor.fetchone()

        if not resultado:
            print("Nenhuma emissão encontrada com o ID informado.")
            return

        print(f"Emissão encontrada: ID: {resultado[0]}, Valor: {resultado[1]:.2f}")

        # Novo valor de emissão
        nova_emissao = validations.validar_numero("Digite o novo valor da emissão de carbono (em toneladas)",
                                                  tipo="float")
        if nova_emissao is None or nova_emissao <= 0:
            print("O valor da emissão deve ser maior que zero.")
            return

        # Atualizar no banco
        cursor.execute("""
            UPDATE tb_emissoes_carbono
            SET emissao = :1
            WHERE id_emissao = :2
        """, [nova_emissao, id_emissao])
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Emissão de carbono alterada com sucesso!")
        else:
            print("Nenhuma alteração foi realizada.")
        cursor.close()

    except Exception as e:
        print("Erro ao alterar emissão de carbono:", e)

# DELETE - Excluir Emissão de Carbono
def excluir_emissao():
    try:
        id_emissao = validations.validar_numero("Digite o ID da emissão de carbono que deseja excluir")
        if id_emissao is None:
            return

        # Excluir no banco
        cursor = connection.conn.cursor()
        cursor.execute("""
            DELETE FROM tb_emissoes_carbono
            WHERE id_emissao = :1
        """, [id_emissao])
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Emissão de carbono excluída com sucesso!")
        else:
            print("Nenhuma emissão encontrada com o ID informado.")
        cursor.close()

    except Exception as e:
        print("Erro ao excluir emissão de carbono:", e)
