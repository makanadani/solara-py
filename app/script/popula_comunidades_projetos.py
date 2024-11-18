from app.connection import conn
import random

def gerar_comunidades_projetos():
    cursor = conn.cursor()

    # Recuperar IDs de comunidades disponíveis
    cursor.execute("SELECT id_comunidade FROM tb_comunidades")
    comunidades = [comunidade[0] for comunidade in cursor.fetchall()]
    if not comunidades:
        print("Nenhuma comunidade cadastrada. Cadastre comunidades antes de associar projetos.")
        return []

    cursor.execute("SELECT id_projeto FROM tb_projetos_sustentaveis")
    projetos = [projeto[0] for projeto in cursor.fetchall()]
    if not projetos:
        print("Nenhum projeto cadastrado. Cadastre projetos antes de associar comunidades.")
        return []

    comunidades_projetos = []

    for comunidade_id in comunidades:
        if random.random() <= 0.7:
            num_projetos = random.randint(1, 3)
            projetos_associados = random.sample(projetos, num_projetos)

            for projeto_id in projetos_associados:
                comunidades_projetos.append((comunidade_id, projeto_id))

    cursor.close()
    return comunidades_projetos

def inserir_comunidades_projetos():
    """
    Insere associações entre comunidades e projetos na tabela associativa.
    """
    try:
        cursor = conn.cursor()

        comunidades_projetos = gerar_comunidades_projetos()
        if not comunidades_projetos:
            return

        for comunidade_id, projeto_id in comunidades_projetos:
            cursor.execute("""
                INSERT INTO tb_comunidades_projetos (id_comunidade, id_projeto)
                VALUES (:1, :2)
            """, (comunidade_id, projeto_id))

        conn.commit()
        print(f"{len(comunidades_projetos)} associações inseridas automaticamente com sucesso.")
        cursor.close()
    except Exception as e:
        print("Erro ao popular associações entre comunidades e projetos:", e)
