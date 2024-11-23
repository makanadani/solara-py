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

# CREATE - Inserir Sensor
def inserir_sensor():
    try:
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

        tipo_sensor = validations.validar_opcao(
            "Escolha o tipo de sensor:\n[Produção, Armazenamento, Consumo]",
            ["Produção", "Armazenamento", "Consumo"]
        )
        if tipo_sensor is None:
            return

        cursor.execute("""
            INSERT INTO tb_sensores (id_comunidade, tipo_sensor)
            VALUES (:1, :2, :3)
        """, [id_comunidade, tipo_sensor, descricao_sensor])
        connection.conn.commit()
        print("Sensor inserido com sucesso!")
        cursor.close()

    except Exception as e:
        print("Erro ao inserir sensor:", e)

# READ - Exibir Sensor por ID
def exibir_sensor_por_id():
    try:
        id_sensor = validations.validar_numero("Digite o ID do sensor que deseja consultar")
        if id_sensor is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_sensor, id_comunidade, tipo_sensor
            FROM tb_sensores
            WHERE id_sensor = :1
        """, [id_sensor])
        resultado = cursor.fetchone()
        cursor.close()

        if resultado:
            print(f"ID: {resultado[0]}, Comunidade ID: {resultado[1]}, Tipo: {resultado[2]}")
        else:
            print("Nenhum sensor encontrado com o ID informado.")

    except Exception as e:
        print("Erro ao consultar sensor:", e)

# READ - Exibir Todos os Sensores
def exibir_todos_sensores():
    try:
        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_sensor, id_comunidade, tipo_sensor
            FROM tb_sensores
            ORDER BY id_sensor ASC
        """)
        sensores = cursor.fetchall()
        cursor.close()

        if sensores:
            print("| ID  | Comunidade ID | Tipo do Sensor    | Descrição                     |")
            print("|-----|---------------|------------------|-------------------------------|")
            for sensor in sensores:
                print(f"| {sensor[0]:<4} | {sensor[1]:<13} | {sensor[2]:<16} | {sensor[3]:<29} |")
        else:
            print("Nenhum sensor cadastrado.")

    except Exception as e:
        print("Erro ao listar todos os sensores:", e)

# UPDATE - Alterar Sensor
def alterar_sensor():
    try:
        id_sensor = validations.validar_numero("Digite o ID do sensor que deseja alterar")
        if id_sensor is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_sensor, tipo_sensor, descricao_sensaor
            FROM tb_sensores
            WHERE id_sensor = :1
        """, [id_sensor])
        sensor = cursor.fetchone()

        if not sensor:
            print("Nenhum sensor encontrado com o ID informado.")
            return

        print(f"Sensor encontrado: ID: {sensor[0]}, Tipo: {sensor[1]}, Descrição: {sensor[2]}")

        novo_tipo = validations.validar_opcao(
            "Escolha o novo tipo de sensor (ou deixe vazio para não alterar):\n[Produção, Armazenamento, Consumo]",
            ["Produção", "Armazenamento", "Consumo"], permitir_vazio=True
        )

        nova_descricao = validations.validar_texto(
            "Digite a nova descrição do sensor (ou deixe vazio para não alterar)", permitir_vazio=True
        )

        query = "UPDATE tb_sensores SET "
        params = []

        if novo_tipo:
            query += "tipo_sensor = :1, "
            params.append(novo_tipo)
        if nova_descricao:
            query += "descricao_sensaor = :2, "
            params.append(nova_descricao)

        if not params:
            print("Nenhuma alteração foi feita.")
            return

        query = query.rstrip(", ") + " WHERE id_sensor = :3"
        params.append(id_sensor)

        cursor.execute(query, params)
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Sensor alterado com sucesso!")
        else:
            print("Nenhuma alteração foi realizada.")
        cursor.close()

    except Exception as e:
        print("Erro ao alterar sensor:", e)

# DELETE - Excluir Sensor
def excluir_sensor():
    try:
        id_sensor = validations.validar_numero("Digite o ID do sensor que deseja excluir")
        if id_sensor is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            DELETE FROM tb_sensores
            WHERE id_sensor = :1
        """, [id_sensor])
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Sensor excluído com sucesso!")
        else:
            print("Nenhum sensor encontrado com o ID informado.")
        cursor.close()

    except Exception as e:
        print("Erro ao excluir sensor:", e)
