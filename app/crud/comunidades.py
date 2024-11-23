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
        while True:
            nome_comunidade = input("Digite o nome da comunidade (ou 'V' para voltar): ").strip()
            if nome_comunidade.upper() == "V":
                print("Voltando ao menu anterior...")
                return
            if nome_comunidade:
                break
            print("O nome da comunidade não pode estar vazio.")

        while True:
            entrada = input("Digite a latitude da comunidade (Formato: 00,00000) (ou 'V' para voltar): ").strip()
            if entrada.upper() == "V":
                print("Voltando ao menu anterior...")
                return
            try:
                latitude = float(entrada)
                if -90 <= latitude <= 90:
                    break
                else:
                    print("A latitude deve estar entre -90 e 90 graus.")
            except ValueError:
                print("Entrada inválida. Insira um número no formato correto.")

        while True:
            entrada = input("Digite a longitude da comunidade (Formato: 000,00000) (ou 'V' para voltar): ").strip()
            if entrada.upper() == "V":
                print("Voltando ao menu anterior...")
                return
            try:
                longitude = float(entrada)
                if -180 <= longitude <= 180:
                    break
                else:
                    print("A longitude deve estar entre -180 e 180 graus.")
            except ValueError:
                print("Entrada inválida. Insira um número no formato correto.")

        cursor = connection.conn.cursor()
        cursor.execute("SELECT id_empresa, nome_empresa FROM tb_empresas")
        empresas = cursor.fetchall()

        if not empresas:
            print("Nenhuma empresa cadastrada.")
            return

        print("| ID | Nome da Empresa |")
        for empresa in empresas:
            print(f"| {empresa[0]:<2} | {empresa[1]:<20} |")

        while True:
            entrada = input("ID da empresa associada à comunidade (ou 'V' para voltar): ").strip()
            if entrada.upper() == "V":
                print("Voltando ao menu anterior...")
                return
            try:
                id_empresa = int(entrada)
                if id_empresa in [empresa[0] for empresa in empresas]:
                    break
                else:
                    print("ID inválido. Escolha um ID listado.")
            except ValueError:
                print("Entrada inválida. Insira um número válido.")

        cursor.execute("SELECT id_regiao, nome_regiao FROM tb_regioes_sustentaveis")
        regioes = cursor.fetchall()

        if not regioes:
            print("Nenhuma região cadastrada.")
            return

        print("| ID | Nome da Região |")
        for regiao in regioes:
            print(f"| {regiao[0]:<2} | {regiao[1]:<15} |")

        while True:
            entrada = input("ID da região associada (ou 'V' para voltar): ").strip()
            if entrada.upper() == "V":
                print("Voltando ao menu anterior...")
                return
            try:
                id_regiao = int(entrada)
                if id_regiao in [regiao[0] for regiao in regioes]:
                    break
                else:
                    print("ID inválido. Escolha um ID listado.")
            except ValueError:
                print("Entrada inválida. Insira um número válido.")

        cursor.execute("""
            INSERT INTO tb_comunidades (id_empresa, id_regiao, nome_comunidade, latitude_comunidade, longitude_comunidade)
            VALUES (:1, :2, :3, :4, :5)
        """, [id_empresa, id_regiao, nome_comunidade, latitude, longitude])

        connection.conn.commit()
        print(f"Comunidade '{nome_comunidade}' inserida com sucesso!")

        cursor.execute("""
            SELECT * FROM tb_comunidades
            WHERE nome_comunidade = :1
        """, [nome_comunidade])
        comunidade_inserida = cursor.fetchone()

        if comunidade_inserida:
            print("Dados da Comunidade Adicionada:")
            print(f"ID: {comunidade_inserida[0]}")
            print(f"Nome: {comunidade_inserida[1]}")
            print(f"Latitude: {comunidade_inserida[2]}")
            print(f"Longitude: {comunidade_inserida[3]}")
            print(f"Empresa Associada: {comunidade_inserida[4]}")
            print(f"Região Associada: {comunidade_inserida[5]}")

        cursor.close()

    except Exception as e:
        print("Erro ao inserir comunidade:", e)


# READ - Exibir Comunidade por ID
def exibir_comunidade_por_id():
    try:
        while True:
            entrada = input("Digite o ID da comunidade (ou 'V' para voltar): ").strip()
            if entrada.upper() == "V":
                print("Voltando ao menu anterior...")
                return
            try:
                id_comunidade = int(entrada)
                break
            except ValueError:
                print("Entrada inválida. Insira um número inteiro válido.")

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_comunidade, nome_comunidade, latitude_comunidade, longitude_comunidade, id_empresa, id_regiao
            FROM tb_comunidades
            WHERE id_comunidade = :1
        """, [id_comunidade])
        comunidade = cursor.fetchone()
        cursor.close()

        if comunidade:
            print(f"ID: {comunidade[0]}")
            print(f"Nome: {comunidade[1]}")
            print(f"Latitude: {comunidade[2]}")
            print(f"Longitude: {comunidade[3]}")
            print(f"Empresa ID: {comunidade[4]}")
            print(f"Região ID: {comunidade[5]}")
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
                    f"| {comunidade[0]:<4} | {comunidade[1]:<20} | {comunidade[2]:<10.5f} | {comunidade[3]:<10.5f} | {comunidade[4]:<10} | {comunidade[5]:<9} |"
                )
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

        novo_nome = validations.validar_texto("Novo nome da comunidade (ou deixe vazio para não alterar)",
                                              permitir_vazio=True)
        nova_latitude = validations.validar_numero("Nova latitude da comunidade (ou deixe vazio para não alterar)",
                                                   tipo="float", permitir_vazio=True)
        nova_longitude = validations.validar_numero("Nova longitude da comunidade (ou deixe vazio para não alterar)",
                                                    tipo="float", permitir_vazio=True)

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
