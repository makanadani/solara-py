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

# CREATE - Inserir Medição
def inserir_medicao():
    try:
        # Exibir comunidades disponíveis
        cursor = connection.conn.cursor()
        cursor.execute("SELECT id_comunidade, nome_comunidade FROM tb_comunidades")
        comunidades = cursor.fetchall()

        if not comunidades:
            print("Nenhuma comunidade disponível. Cadastre uma comunidade antes.")
            return

        print("| ID  | Nome da Comunidade          |")
        for comunidade in comunidades:
            print(f"| {comunidade[0]:<4} | {comunidade[1]:<26} |")

        id_comunidade = validations.validar_id_existente(
            "Digite o ID da comunidade associada", [com[0] for com in comunidades]
        )
        if id_comunidade is None:
            return

        # Exibir sensores disponíveis para a comunidade
        cursor.execute("""
            SELECT id_sensor, tipo_sensor, descricao_sensaor
            FROM tb_sensores
            WHERE id_comunidade = :1
        """, [id_comunidade])
        sensores = cursor.fetchall()

        if not sensores:
            print("Nenhum sensor disponível para a comunidade selecionada.")
            return

        print("| ID  | Tipo do Sensor    | Descrição                     |")
        for sensor in sensores:
            print(f"| {sensor[0]:<4} | {sensor[1]:<17} | {sensor[2]:<28} |")

        id_sensor = validations.validar_id_existente(
            "Digite o ID do sensor associado", [sensor[0] for sensor in sensores]
        )
        if id_sensor is None:
            return

        # Obter tipo de medição
        tipo_medicao = validations.validar_opcao(
            "Escolha o tipo de medição:\n[Produção, Armazenamento, Consumo]",
            ["Produção", "Armazenamento", "Consumo"]
        )
        if tipo_medicao is None:
            return

        # Valor da medição
        valor_medicao = validations.validar_numero("Digite o valor da medição", tipo="float")
        if valor_medicao is None or valor_medicao <= 0:
            print("O valor da medição deve ser maior que zero.")
            return

        # Inserir no banco
        cursor.execute("""
            INSERT INTO tb_medicoes (id_comunidade, id_sensor, tipo_medicao, valor_medicao)
            VALUES (:1, :2, :3, :4)
        """, [id_comunidade, id_sensor, tipo_medicao, valor_medicao])
        connection.conn.commit()
        print("Medição inserida com sucesso!")
        cursor.close()

    except Exception as e:
        print("Erro ao inserir medição:", e)

# READ - Exibir Medição por ID
def exibir_medicao_por_id():
    try:
        id_medicao = validations.validar_numero("Digite o ID da medição que deseja consultar")
        if id_medicao is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_medicao, id_comunidade, id_sensor, tipo_medicao, valor_medicao, data_hora_medicao
            FROM tb_medicoes
            WHERE id_medicao = :1
        """, [id_medicao])
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            print(f"ID: {resultado[0]}, Comunidade ID: {resultado[1]}, Sensor ID: {resultado[2]}, "
                  f"Tipo: {resultado[3]}, Valor: {resultado[4]:.2f}, Data/Hora: {resultado[5]}")
        else:
            print("Nenhuma medição encontrada com o ID informado.")

    except Exception as e:
        print("Erro ao consultar medição:", e)

# READ - Exibir Todas as Medições
def exibir_todas_medicoes():
    try:
        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_medicao, id_comunidade, id_sensor, tipo_medicao, valor_medicao, data_hora_medicao
            FROM tb_medicoes
            ORDER BY id_medicao ASC
        """)
        medicoes = cursor.fetchall()
        cursor.close()

        if medicoes:
            print("| ID  | Comunidade ID | Sensor ID | Tipo Medição     | Valor    | Data/Hora               |")
            print("|-----|---------------|-----------|------------------|----------|-------------------------|")
            for medicao in medicoes:
                print(
                    f"| {medicao[0]:<4} | {medicao[1]:<13} | {medicao[2]:<9} | {medicao[3]:<16} | {medicao[4]:<8.2f} | {medicao[5]} |")
        else:
            print("Nenhuma medição cadastrada.")

    except Exception as e:
        print("Erro ao listar todas as medições:", e)

# UPDATE - Alterar Medição
def alterar_medicao():
    try:
        id_medicao = validations.validar_numero("Digite o ID da medição que deseja alterar")
        if id_medicao is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_medicao, tipo_medicao, valor_medicao
            FROM tb_medicoes
            WHERE id_medicao = :1
        """, [id_medicao])
        medicao = cursor.fetchone()

        if not medicao:
            print("Nenhuma medição encontrada com o ID informado.")
            return

        print(f"Medição encontrada: ID: {medicao[0]}, Tipo: {medicao[1]}, Valor: {medicao[2]:.2f}")

        # Novo valor da medição
        novo_valor = validations.validar_numero("Digite o novo valor da medição (ou deixe vazio para não alterar)",
                                                tipo="float", permitir_vazio=True)

        # Novo tipo de medição
        novo_tipo = validations.validar_opcao(
            "Escolha o novo tipo de medição (ou deixe vazio para não alterar):\n[Produção, Armazenamento, Consumo]",
            ["Produção", "Armazenamento", "Consumo"]
        )

        # Montar query dinamicamente
        query = "UPDATE tb_medicoes SET "
        params = []

        if novo_valor:
            query += "valor_medicao = :1, "
            params.append(novo_valor)
        if novo_tipo:
            query += "tipo_medicao = :2, "
            params.append(novo_tipo)

        if not params:
            print("Nenhuma alteração foi feita.")
            return

        query = query.rstrip(", ") + " WHERE id_medicao = :3"
        params.append(id_medicao)

        # Executar atualização
        cursor.execute(query, params)
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Medição alterada com sucesso!")
        else:
            print("Nenhuma alteração foi realizada.")
        cursor.close()

    except Exception as e:
        print("Erro ao alterar medição:", e)

# DELETE - Excluir Medição
def excluir_medicao():
    try:
        id_medicao = validations.validar_numero("Digite o ID da medição que deseja excluir")
        if id_medicao is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            DELETE FROM tb_medicoes
            WHERE id_medicao = :1
        """, [id_medicao])
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Medição excluída com sucesso!")
        else:
            print("Nenhuma medição encontrada com o ID informado.")
        cursor.close()

    except Exception as e:
        print("Erro ao excluir medição:", e)
