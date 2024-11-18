import random

from app.connection import conn

def gerar_sensores(quantidade):
    """
    Gera sensores fictícios associados a comunidades e tipos de fonte.
    """
    cursor = conn.cursor()

    cursor.execute("SELECT id_comunidade FROM tb_comunidades")
    comunidades = [com[0] for com in cursor.fetchall()]
    if not comunidades:
        print("Nenhuma comunidade cadastrada. Cadastre comunidades antes de popular sensores.")
        return []

    cursor.execute("SELECT id_tipo_fonte FROM tb_tipo_fontes")
    tipos_fontes = [fonte[0] for fonte in cursor.fetchall()]
    if not tipos_fontes:
        print("Nenhum tipo de fonte cadastrado. Cadastre tipos de fonte antes de popular sensores.")
        return []

    tipos_sensores = ["Produção", "Armazenamento", "Consumo"]

    sensores = []
    for _ in range(quantidade):
        id_comunidade = random.choice(comunidades)
        id_tipo_fonte = random.choice(tipos_fontes)
        tipo_sensor = random.choice(tipos_sensores)
        descricao_sensor = f"Sensor de {tipo_sensor.lower()} associado à fonte {id_tipo_fonte}"

        sensores.append((id_comunidade, id_tipo_fonte, tipo_sensor, descricao_sensor))

    cursor.close()
    return sensores

def inserir_sensores(quantidade):
    """
    Insere sensores gerados automaticamente na tabela TB_SENSORES.
    """
    try:
        cursor = conn.cursor()
        sensores = gerar_sensores(quantidade)
        if not sensores:
            return

        for sensor in sensores:
            cursor.execute("""
                INSERT INTO tb_sensores (id_comunidade, id_tipo_fonte, tipo_sensor, descricao_sensaor)
                VALUES (:1, :2, :3, :4)
            """, sensor)

        conn.commit()
        print(f"{quantidade} sensores inseridos automaticamente com sucesso.")
        cursor.close()
    except Exception as e:
        print(f"Erro ao popular sensores: {e}")
