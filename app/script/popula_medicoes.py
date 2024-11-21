import random
from datetime import datetime, timedelta

from app.connection import conn


def gerar_valor_producao(tipo_fonte, hora):
    if tipo_fonte == 1:  # Solar
        if 8 <= hora <= 16:
            return random.randint(300, 500)  # Pico solar
        else:
            return random.randint(0, 50)  # Noite
    elif tipo_fonte == 2:  # Eólica
        return random.randint(100, 600)  # Variável
    elif tipo_fonte == 3:  # Hidrelétrica
        return random.randint(500, 1500)  # Constante
    elif tipo_fonte == 4:  # Geotérmica
        return random.randint(300, 800)  # Constante
    elif tipo_fonte == 5:  # Biomassa
        return random.randint(200, 700)  # Estável
    return 0


def gerar_medicoes_diarias():
    cursor = conn.cursor()

    # Recuperar todos os sensores com o tipo de fonte
    cursor.execute("SELECT id_sensor, tipo_sensor, id_tipo_fonte FROM tb_sensores")
    sensores = cursor.fetchall()
    if not sensores:
        print("Nenhum sensor cadastrado.")
        return []

    medicoes = []
    data_inicio = datetime.now() - timedelta(days=7)  # Gerar medições dos últimos 7 dias
    data_fim = datetime.now()

    producoes = {}
    consumos = {}

    # Iterar por todos os dias no intervalo
    data_atual = data_inicio
    while data_atual <= data_fim:
        for hora in range(0, 24, 6):  # Medições a cada 6 horas
            for id_sensor, tipo_sensor, id_tipo_fonte in sensores:
                if tipo_sensor == "Produção":
                    valor_producao = gerar_valor_producao(id_tipo_fonte, hora)
                    producoes[id_sensor] = producoes.get(id_sensor, 0) + valor_producao
                    medicoes.append((
                        id_sensor,
                        "Produção",
                        valor_producao,
                        data_atual.replace(hour=hora, minute=0, second=0, microsecond=0)
                    ))
                elif tipo_sensor == "Consumo":
                    valor_consumo = random.randint(30, 150)  # Consumo: valor incremental
                    consumos[id_sensor] = consumos.get(id_sensor, 0) + valor_consumo
                    medicoes.append((
                        id_sensor,
                        "Consumo",
                        valor_consumo,
                        data_atual.replace(hour=hora, minute=0, second=0, microsecond=0)
                    ))
                elif tipo_sensor == "Armazenamento":
                    # Armazenamento = Total Produzido - Total Consumido
                    valor_armazenamento = producoes.get(id_sensor, 0) - consumos.get(id_sensor, 0)

                    # Registrar valor negativo no console como alerta
                    if valor_armazenamento < 0:
                        print(f"ALERTA: Déficit de energia detectado! "
                              f"Sensor ID: {id_sensor}, Data: {data_atual.strftime('%Y-%m-%d %H:%M:%S')}, "
                              f"Déficit: {valor_armazenamento}")

                    # Registrar o valor no banco de dados, mesmo que negativo
                    medicoes.append((
                        id_sensor,
                        "Armazenamento",
                        valor_armazenamento,
                        data_atual.replace(hour=hora, minute=0, second=0)
                    ))

        data_atual += timedelta(days=1)

    cursor.close()
    return medicoes


def inserir_medicoes():
    try:
        cursor = conn.cursor()
        medicoes = gerar_medicoes_diarias()
        if not medicoes:
            return

        for id_sensor, tipo_medicao, valor_medicao, data_hora_medicao in medicoes:
            cursor.execute("""
                INSERT INTO tb_medicoes (id_sensor, tipo_medicao, valor_medicao, data_hora_medicao)
                VALUES (:1, :2, :3, :4)
            """, (id_sensor, tipo_medicao, valor_medicao, data_hora_medicao))

        conn.commit()
        print(f"{len(medicoes)} medições inseridas automaticamente com sucesso.")
        cursor.close()
    except Exception as e:
        print(f"Erro ao popular medições: {e}")
