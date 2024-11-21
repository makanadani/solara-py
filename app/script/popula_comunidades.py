comunidades_indigenas = {
    1: [  # Norte
        {"nome": "Yanomami", "latitude": 1.6957, "longitude": -63.0678},
        {"nome": "Ticuna", "latitude": -3.7667, "longitude": -70.2667},
        {"nome": "Kayapó", "latitude": -7.8841, "longitude": -51.8455},
        {"nome": "Waiãpi", "latitude": 0.8471, "longitude": -52.1083},
        {"nome": "Munduruku", "latitude": -6.1538, "longitude": -56.8028},
        {"nome": "Araweté", "latitude": -3.7856, "longitude": -52.4828},
        {"nome": "Zo'é", "latitude": -0.8333, "longitude": -54.6667},
        {"nome": "Arara", "latitude": -5.8203, "longitude": -52.7621},
        {"nome": "Suruwahá", "latitude": -7.9467, "longitude": -67.8483},
        {"nome": "Javari", "latitude": -4.3058, "longitude": -71.7144},
    ],
    2: [  # Sul
        {"nome": "Kaingang", "latitude": -27.5916, "longitude": -51.7067},
        {"nome": "Guarani Mbya", "latitude": -25.4284, "longitude": -49.2733},
        {"nome": "Xokleng", "latitude": -26.9597, "longitude": -49.5542},
        {"nome": "Charrua", "latitude": -28.0500, "longitude": -52.0167},
        {"nome": "Mbya Guarani", "latitude": -29.7956, "longitude": -51.1448},
        {"nome": "Kaingang Campo do Meio", "latitude": -27.5000, "longitude": -52.0000},
        {"nome": "Lagoa dos Patos", "latitude": -31.9455, "longitude": -52.3266},
        {"nome": "Votouro", "latitude": -27.1333, "longitude": -52.2667},
        {"nome": "Ligeiro", "latitude": -27.7167, "longitude": -50.5000},
        {"nome": "Nonoai", "latitude": -27.3569, "longitude": -52.7756},
    ],
    3: [  # Leste
        {"nome": "Pataxó", "latitude": -16.4090, "longitude": -39.0771},
        {"nome": "Tupinambá", "latitude": -14.7903, "longitude": -39.2802},
        {"nome": "Maxakali", "latitude": -17.5146, "longitude": -41.1176},
        {"nome": "Krenak", "latitude": -19.5330, "longitude": -42.6438},
        {"nome": "Pankararé", "latitude": -9.1261, "longitude": -38.2315},
        {"nome": "Pankararu", "latitude": -9.0857, "longitude": -38.2463},
        {"nome": "Tumbalalá", "latitude": -8.7218, "longitude": -39.3186},
        {"nome": "Atikum", "latitude": -8.7613, "longitude": -38.2168},
        {"nome": "Tupiniquim", "latitude": -20.3155, "longitude": -40.2955},
        {"nome": "Botocudo", "latitude": -19.8697, "longitude": -41.8066},
    ],
    4: [  # Oeste
        {"nome": "Bororo", "latitude": -15.2265, "longitude": -56.6538},
        {"nome": "Terena", "latitude": -20.4697, "longitude": -54.6201},
        {"nome": "Kadiwéu", "latitude": -20.8374, "longitude": -57.5231},
        {"nome": "Ofaié", "latitude": -19.4667, "longitude": -51.5667},
        {"nome": "Guató", "latitude": -17.8586, "longitude": -57.7578},
        {"nome": "Arara do Rio Branco", "latitude": -15.6738, "longitude": -58.2642},
        {"nome": "Paresi", "latitude": -14.6678, "longitude": -57.1500},
        {"nome": "Chiquitano", "latitude": -16.3667, "longitude": -58.3333},
        {"nome": "Nambikwara", "latitude": -13.1096, "longitude": -59.2090},
        {"nome": "Bakairi", "latitude": -14.7867, "longitude": -54.4700},
    ],
    5: [  # Centro-Oeste
        {"nome": "Xavante", "latitude": -14.6507, "longitude": -52.3507},
        {"nome": "Karajá", "latitude": -10.1835, "longitude": -50.3227},
        {"nome": "Kayabi", "latitude": -11.6016, "longitude": -55.8430},
        {"nome": "Javaé", "latitude": -11.7853, "longitude": -49.5331},
        {"nome": "Tapirapé", "latitude": -11.2458, "longitude": -51.5653},
        {"nome": "Bororo Central", "latitude": -16.3483, "longitude": -54.6358},
        {"nome": "Guarani Kaiowá", "latitude": -23.5377, "longitude": -54.7593},
        {"nome": "Ofayé", "latitude": -19.2344, "longitude": -54.7456},
        {"nome": "Guató Pantanal", "latitude": -17.3578, "longitude": -57.4598},
        {"nome": "Krahô", "latitude": -8.3525, "longitude": -47.6044},
    ],
}

import random

from app.connection import conn


def gerar_comunidades():
    cursor = conn.cursor()

    # Recupera IDs de empresas cadastradas
    cursor.execute("SELECT id_empresa FROM tb_empresas")
    empresas = [empresa[0] for empresa in cursor.fetchall()]
    if not empresas:
        print("Nenhuma empresa cadastrada. Cadastre empresas antes de popular comunidades.")
        return []

    # Recupera IDs de regiões cadastradas
    cursor.execute("SELECT id_regiao FROM tb_regioes_sustentaveis")
    regioes = [regiao[0] for regiao in cursor.fetchall()]
    if not regioes:
        print("Nenhuma região cadastrada. Cadastre regiões antes de popular comunidades.")
        return []

    comunidades = []
    comunidades_usadas = set()

    for id_regiao in regioes:
        if id_regiao not in comunidades_indigenas:
            continue

        # Para cada comunidade na região
        for comunidade in comunidades_indigenas[id_regiao]:
            comunidade_key = (id_regiao, comunidade["nome"])

            # Evitar duplicatas se já usada
            if comunidade_key in comunidades_usadas:
                continue

            # Seleciona uma empresa aleatoriamente para associar à comunidade
            id_empresa = random.choice(empresas)

            # Gera um protocolo único
            protocolo = random.randint(100000, 999999)

            # Adiciona a comunidade ao resultado
            comunidades.append((
                id_empresa,
                id_regiao,
                protocolo,
                comunidade["nome"],
                comunidade["latitude"],
                comunidade["longitude"]
            ))

            # Marca a comunidade como usada
            comunidades_usadas.add(comunidade_key)

    cursor.close()
    return comunidades

def inserir_comunidades():
    try:
        cursor = conn.cursor()

        # Gera as comunidades
        comunidades = gerar_comunidades()
        if not comunidades:
            return

        # Insere comunidades no banco de dados
        for comunidade in comunidades:
            cursor.execute("""
                INSERT INTO tb_comunidades (
                    id_empresa,
                    id_regiao,
                    protocolo_atendimento_comunidade,
                    nome_comunidade,
                    latitude_comunidade,
                    longitude_comunidade
                ) VALUES (:1, :2, :3, :4, :5, :6)
            """, comunidade)

        conn.commit()
        print(f"{len(comunidades)} comunidades inseridas automaticamente com sucesso.")
        cursor.close()
    except Exception as e:
        print("Erro ao popular comunidades:", e)
