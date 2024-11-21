import random

from app.connection import conn


def gerar_comunidades_projetos():
    cursor = conn.cursor()

    # Recuperar IDs de comunidades disponíveis
    cursor.execute("SELECT id_comunidade FROM tb_comunidades")
    comunidades = [comunidade[0] for comunidade in cursor.fetchall()]
    if not comunidades:
        print("Nenhuma comunidade cadastrada.")
        return []

    # Recuperar IDs e descrições dos projetos disponíveis
    cursor.execute("SELECT id_projeto, descricao_projeto FROM tb_projetos_sustentaveis")
    projetos = cursor.fetchall()
    if not projetos:
        print("Nenhum projeto cadastrado.")
        return []

    comunidades_projetos = []

    for comunidade_id in comunidades:
        if random.random() <= 0.7:  # 70% de chance de associar projetos a uma comunidade
            num_projetos = random.randint(1, 3)
            projetos_associados = random.sample(projetos, num_projetos)

            for projeto_id, descricao_projeto in projetos_associados:
                # Evita NULL nas descrições
                descricao_projeto = descricao_projeto or "Descrição Padrão"

                # Verificar se já existe a mesma descrição para a comunidade
                cursor.execute("""
                    SELECT COUNT(*)
                    FROM tb_comunidades_projetos cp
                    JOIN tb_projetos_sustentaveis ps ON cp.id_projeto = ps.id_projeto
                    WHERE cp.id_comunidade = :1 AND ps.descricao_projeto = :2
                """, (comunidade_id, descricao_projeto))

                if cursor.fetchone()[0] == 0:  # Inserir apenas se não existir
                    comunidades_projetos.append({
                        "id_comunidade": comunidade_id,
                        "id_projeto": projeto_id
                    })

    cursor.close()
    return comunidades_projetos


def inserir_comunidades_projetos(comunidades_projetos):
    try:
        cursor = conn.cursor()

        for item in comunidades_projetos:
            id_comunidade = item["id_comunidade"]
            id_projeto = item["id_projeto"]

            # Obter a descrição do projeto pelo ID
            cursor.execute("""
                SELECT descricao_projeto FROM tb_projetos_sustentaveis
                WHERE id_projeto = :1
            """, (id_projeto,))
            descricao_projeto = cursor.fetchone()
            if not descricao_projeto:
                print(f"Projeto {id_projeto} não encontrado. Ignorando.")
                continue
            descricao_projeto = descricao_projeto[0]

            # Verificar se a mesma descrição já está associada à comunidade
            cursor.execute("""
                SELECT COUNT(*)
                FROM tb_comunidades_projetos cp
                JOIN tb_projetos_sustentaveis ps ON cp.id_projeto = ps.id_projeto
                WHERE cp.id_comunidade = :1 AND ps.descricao_projeto = :2
            """, (id_comunidade, descricao_projeto))

            if cursor.fetchone()[0] > 0:
                print(f"A mesma descrição '{descricao_projeto}' já está associada à comunidade {id_comunidade}. Ignorando.")
                continue

            # Inserir a associação se não existir
            cursor.execute("""
                INSERT INTO tb_comunidades_projetos (id_comunidade, id_projeto)
                VALUES (:1, :2)
            """, (id_comunidade, id_projeto))

        conn.commit()
        print(f"{len(comunidades_projetos)} associações processadas com sucesso.")
        cursor.close()

    except Exception as e:
        print(f"Erro ao popular associações entre comunidades e projetos: {e}")

