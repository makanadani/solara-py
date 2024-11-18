import random

from app.connection import conn

def gerar_medicoes(quantidade):
    """
    Gera medições fictícias associadas a sensores e comunidades.
    """
    cursor = conn.cursor()

    cursor.execute("SELECT id_sensor, id_comunidade FROM tb_sensores")
    sensores = cursor.fetchall()
    if not sensores:
        print("Nenhum sensor cadastrado. Cadastre sensores antes de popular medições.")
        return []

    tipos_medicao = ["Produção", "Armazenamento", "Consumo"]
    medicoes = []

    for _ in range(quantidade):
        sensor = random.choice(sensores)
        id_sensor = sensor[0]
        id_comunidade = sensor[1]
        tipo_medicao = random.choice(tipos_medicao)
        valor_medicao = random.randint(1, 1000)  # Valor fictício

        medicoes.append((id_comunidade, id_sensor, tipo_medicao, valor_medicao))

    cursor.close()
    return medicoes

def inserir_medicoes(quantidade):
    """
    Insere medições geradas automaticamente na tabela TB_MEDICOES.
    """
    try:
        cursor = conn.cursor()
        medicoes = gerar_medicoes(quantidade)
        if not medicoes:
            return

        for medicao in medicoes:
            cursor.execute("""
                INSERT INTO tb_medicoes (id_comunidade, id_sensor, tipo_medicao, valor_medicao)
                VALUES (:1, :2, :3, :4)
            """, medicao)

        conn.commit()
        print(f"{quantidade} medições inseridas automaticamente com sucesso.")
        cursor.close()
    except Exception as e:
        print(f"Erro ao popular medições: {e}")
