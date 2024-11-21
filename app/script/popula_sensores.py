import random

from app.connection import conn


def gerar_sensores():
    cursor = conn.cursor()

    # Recupera todas as comunidades cadastradas
    cursor.execute("SELECT id_comunidade FROM tb_comunidades")
    comunidades = [com[0] for com in cursor.fetchall()]
    if not comunidades:
        print("Nenhuma comunidade cadastrada.")
        return []

    # Recupera todos os tipos de fontes cadastrados
    cursor.execute("SELECT id_tipo_fonte FROM tb_tipo_fontes")
    tipos_fontes = [fonte[0] for fonte in cursor.fetchall()]
    if not tipos_fontes:
        print("Nenhum tipo de fonte cadastrado.")
        return []

    sensores = []

    # Garante que cada comunidade tenha 3 sensores de Produção, 3 de Consumo e 1 de Armazenamento
    for id_comunidade in comunidades:
        # Adiciona 3 sensores de Produção
        for _ in range(3):
            id_tipo_fonte = random.choice(tipos_fontes)  # Produção exige id_tipo_fonte
            sensores.append((id_comunidade, id_tipo_fonte, "Produção"))

        # Adiciona 3 sensores de Consumo
        for _ in range(3):
            sensores.append((id_comunidade, None, "Consumo"))

        # Adiciona 1 sensor de Armazenamento
        sensores.append((id_comunidade, None, "Armazenamento"))

    cursor.close()
    return sensores

def inserir_sensores():
    try:
        cursor = conn.cursor()

        # Gera sensores para todas as comunidades
        sensores = gerar_sensores()
        if not sensores:
            return

        # Insere os sensores no banco de dados
        for sensor in sensores:
            cursor.execute("""
                INSERT INTO tb_sensores (id_comunidade, id_tipo_fonte, tipo_sensor)
                VALUES (:1, :2, :3)
            """, sensor)

        conn.commit()
        print(f"{len(sensores)} sensores inseridos automaticamente com sucesso.")
        cursor.close()
    except Exception as e:
        print(f"Erro ao popular sensores: {e}")
