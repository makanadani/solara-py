empresas_reais = [
    {"nome": "BRENCO Companhia Brasileira de Energia Renovável", "cnpj": "08.070.566/0001-00"},
    {"nome": "Siemens Gamesa Energia Renovável Ltda", "cnpj": "10.467.863/0001-12"},
    {"nome": "Atlas Energia Renovável do Brasil S.A.", "cnpj": "28.892.485/0001-00"},
    {"nome": "CPFL Energias Renováveis S.A.", "cnpj": "08.439.659/0001-50"},
    {"nome": "Engie Brasil Energia S.A.", "cnpj": "02.474.103/0001-19"},
    {"nome": "Omega Energia S.A.", "cnpj": "10.456.781/0001-51"},
    {"nome": "EDP Renováveis Brasil S.A.", "cnpj": "12.345.678/0001-90"},
    {"nome": "Statkraft Energias Renováveis Ltda", "cnpj": "15.678.901/0001-23"},
    {"nome": "Ibitu Energia S.A.", "cnpj": "17.890.123/0001-45"},
    {"nome": "Elera Renováveis S.A.", "cnpj": "19.012.345/0001-67"},
    {"nome": "Ventos do Sul Energia S.A.", "cnpj": "27.890.678/0001-89"},
    {"nome": "Neoenergia Renováveis Ltda", "cnpj": "33.789.012/0001-34"},
    {"nome": "Solatio Energia S.A.", "cnpj": "44.789.123/0001-56"},
    {"nome": "Casa dos Ventos Energias Renováveis S.A.", "cnpj": "55.890.234/0001-78"},
    {"nome": "Energia Sustentável do Brasil S.A.", "cnpj": "66.901.345/0001-89"},
    {"nome": "Renova Energia S.A.", "cnpj": "77.123.456/0001-67"},
    {"nome": "Voltalia Energia Renovável Ltda", "cnpj": "88.345.567/0001-89"},
    {"nome": "Votorantim Energia S.A.", "cnpj": "99.567.678/0001-90"},
    {"nome": "Brookfield Energia Renovável Ltda", "cnpj": "11.789.890/0001-12"},
    {"nome": "Terra Alta Energias Renováveis S.A.", "cnpj": "22.901.012/0001-34"},
]

def inserir_empresas(empresas):
    """
    Insere empresas reais na tabela tb_empresas.
    """
    from app.connection import conn
    import random

    try:
        cursor = conn.cursor()

        for empresa in empresas:
            nome_empresa = empresa["nome"]
            cnpj_empresa = empresa["cnpj"].replace(".", "").replace("/", "").replace("-", "")
            senha_empresa = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*", k=12))  # Gera senha aleatória

            cursor.execute("""
                INSERT INTO tb_empresas (nome_empresa, cnpj_empresa, senha_empresa)
                VALUES (:1, :2, :3)
            """, (nome_empresa, cnpj_empresa, senha_empresa))

        conn.commit()
        print(f"{len(empresas)} empresas inseridas com sucesso.")
        cursor.close()
    except Exception as e:
        print(f"Erro ao inserir empresas reais: {e}")