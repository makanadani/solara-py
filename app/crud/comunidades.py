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

# CREATE - Inserir Comunidade
def inserir_comunidade():
    try:
        # Nome da comunidade
        nome_comunidade = validations.validar_texto("Digite o nome da comunidade")
        if nome_comunidade is None:
            return

        # Latitude e Longitude
        latitude = validations.validar_numero("Digite a latitude da comunidade", tipo="float")
        if latitude is None:
            return

        longitude = validations.validar_numero("Digite a longitude da comunidade", tipo="float")
        if longitude is None:
            return

        # Empresa associada
        cursor = connection.conn.cursor()
        cursor.execute("SELECT id_empresa, nome_empresa FROM tb_empresas")
        empresas = cursor.fetchall()
        if not empresas:
            print("Nenhuma empresa disponível. Cadastre uma empresa antes.")
            return

        print("| ID | Nome da Empresa |")
        for empresa in empresas:
            print(f"| {empresa[0]:<2} | {empresa[1]:<20} |")

        id_empresa = validations.validar_id_existente(
            "ID da empresa associada", [empresa[0] for empresa in empresas]
        )
        if id_empresa is None:
            return

        # Região associada
        cursor.execute("SELECT id_regiao, nome_regiao FROM tb_regioes_sustentaveis")
        regioes = cursor.fetchall()
        if not regioes:
            print("Nenhuma região disponível. Cadastre uma região antes.")
            return

        print("| ID | Nome da Região |")
        for regiao in regioes:
            print(f"| {regiao[0]:<2} | {regiao[1]:<15} |")

        id_regiao = validations.validar_id_existente(
            "ID da região associada", [regiao[0] for regiao in regioes]
        )
        if id_regiao is None:
            return

        # Inserir no banco
        cursor.execute("""
            INSERT INTO tb_comunidades (id_empresa, id_regiao, nome_comunidade, latitude_comunidade, longitude_comunidade)
            VALUES (:1, :2, :3, :4, :5)
        """, [id_empresa, id_regiao, nome_comunidade, latitude, longitude])
        connection.conn.commit()
        print(f"Comunidade '{nome_comunidade}' inserida com sucesso!")
        cursor.close()

    except Exception as e:
        print("Erro ao inserir comunidade:", e)

# READ - Exibir Comunidade por ID
def exibir_comunidade_por_id():
    try:
        id_comunidade = validations.validar_numero("Digite o ID da comunidade")
        if id_comunidade is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_comunidade, nome_comunidade, latitude_comunidade, longitude_comunidade, id_empresa, id_regiao
            FROM tb_comunidades
            WHERE id_comunidade = :1
        """, [id_comunidade])
        comunidade = cursor.fetchone()
        cursor.close()

        if comunidade:
            print(f"ID: {comunidade[0]}, Nome: {comunidade[1]}, Latitude: {comunidade[2]}, Longitude: {comunidade[3]}, "
                  f"Empresa ID: {comunidade[4]}, Região ID: {comunidade[5]}")
        else:
            print("Nenhuma comunidade encontrada com o ID informado.")

    except Exception as e:
        print("Erro ao buscar a comunidade:", e)


# READ - Exibir Todas as Comunidades
def exibir_todas_comunidades():
    try:
        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_comunidade, nome_comunidade, latitude_comunidade, longitude_comunidade, id_empresa, id_regiao
            FROM tb_comunidades
            ORDER BY id_comunidade ASC
        """)
        comunidades = cursor.fetchall()
        cursor.close()

        if comunidades:
            print("| ID  | Nome da Comunidade   | Latitude   | Longitude  | Empresa ID | Região ID |")
            print("|-----|----------------------|------------|------------|------------|-----------|")
            for comunidade in comunidades:
                print(
                    f"| {comunidade[0]:<4} | {comunidade[1]:<20} | {comunidade[2]:<10.5f} | {comunidade[3]:<10.5f} | {comunidade[4]:<10} | {comunidade[5]:<9} |")
        else:
            print("Nenhuma comunidade cadastrada.")

    except Exception as e:
        print("Erro ao exibir comunidades:", e)


# UPDATE - Alterar Comunidade
def alterar_comunidade():
    try:
        id_comunidade = validations.validar_numero("Digite o ID da comunidade que deseja alterar")
        if id_comunidade is None:
            return

        cursor = connection.conn.cursor()

        # Verificar se a comunidade existe
        cursor.execute("""
            SELECT id_comunidade, nome_comunidade, latitude_comunidade, longitude_comunidade
            FROM tb_comunidades
            WHERE id_comunidade = :1
        """, [id_comunidade])
        comunidade = cursor.fetchone()

        if not comunidade:
            print("Nenhuma comunidade encontrada com o ID informado.")
            return

        print(
            f"Comunidade encontrada: ID: {comunidade[0]}, Nome: {comunidade[1]}, Latitude: {comunidade[2]}, Longitude: {comunidade[3]}")

        # Solicitar novas informações
        novo_nome = validations.validar_texto("Novo nome da comunidade (ou deixe vazio para não alterar)",
                                              permitir_vazio=True)
        nova_latitude = validations.validar_numero("Nova latitude da comunidade (ou deixe vazio para não alterar)",
                                                   tipo="float", permitir_vazio=True)
        nova_longitude = validations.validar_numero("Nova longitude da comunidade (ou deixe vazio para não alterar)",
                                                    tipo="float", permitir_vazio=True)

        # Montar a query dinamicamente
        query = "UPDATE tb_comunidades SET "
        params = []

        if novo_nome:
            query += "nome_comunidade = :1, "
            params.append(novo_nome)
        if nova_latitude:
            query += "latitude_comunidade = :2, "
            params.append(nova_latitude)
        if nova_longitude:
            query += "longitude_comunidade = :3, "
            params.append(nova_longitude)

        if not params:
            print("Nenhuma alteração foi feita.")
            return

        query = query.rstrip(", ")
        query += " WHERE id_comunidade = :4"
        params.append(id_comunidade)

        cursor.execute(query, params)
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Comunidade alterada com sucesso!")
        else:
            print("Nenhuma alteração realizada.")
        cursor.close()

    except Exception as e:
        print("Erro ao alterar comunidade:", e)


# DELETE - Excluir Comunidade
def excluir_comunidade():
    try:
        id_comunidade = validations.validar_numero("Digite o ID da comunidade que deseja excluir")
        if id_comunidade is None:
            return

        cursor = connection.conn.cursor()

        # Verificar dependências
        cursor.execute("""
            SELECT COUNT(*)
            FROM tb_comunidades_projetos
            WHERE id_comunidade = :1
        """, [id_comunidade])
        dependencias = cursor.fetchone()[0]

        if dependencias > 0:
            print(
                f"Não é possível excluir a comunidade com ID {id_comunidade} porque está associada a {dependencias} projeto(s).")
            return

        # Confirmar exclusão
        cursor.execute("""
            SELECT nome_comunidade
            FROM tb_comunidades
            WHERE id_comunidade = :1
        """, [id_comunidade])
        comunidade = cursor.fetchone()

        if not comunidade:
            print("Nenhuma comunidade encontrada com o ID informado.")
            return

        confirmacao = validations.validar_opcao(
            f"Tem certeza que deseja excluir a comunidade '{comunidade[0]}'? [S/N]",
            ["S", "N"]
        )
        if confirmacao == "N":
            print("Operação de exclusão cancelada.")
            return

        # Excluir a comunidade
        cursor.execute("""
            DELETE FROM tb_comunidades
            WHERE id_comunidade = :1
        """, [id_comunidade])
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Comunidade excluída com sucesso!")
        else:
            print("Erro ao excluir a comunidade.")
        cursor.close()

    except Exception as e:
        print("Erro ao excluir a comunidade:", e)
