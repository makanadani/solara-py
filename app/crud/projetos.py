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

# CREATE - Inserir Projeto Sustentável
def inserir_projeto():
    try:
        descricao = validations.validar_texto("Descrição do projeto")
        custo = validations.validar_numero("Custo do projeto", tipo="float")
        status_opcao = validations.validar_opcao(
            "Escolha o status do projeto:\n[1] Em andamento\n[2] Concluído",
            ["1", "2"]
        )
        status = "Em andamento" if status_opcao == "1" else "Concluído"

        cursor = connection.conn.cursor()
        cursor.execute("SELECT id_tipo_fonte, nome_fonte FROM tb_tipo_fontes")
        tipos_fontes = cursor.fetchall()

        id_tipo_fonte = validations.validar_id_existente(
            "ID do tipo de fonte associada", [fonte[0] for fonte in tipos_fontes]
        )

        cursor.execute("SELECT id_comunidade, nome_comunidade FROM tb_comunidades")
        comunidades = cursor.fetchall()

        id_comunidade = validations.validar_id_existente(
            "ID da comunidade associada", [com[0] for com in comunidades]
        )

        cursor.execute("""
            INSERT INTO tb_projetos_sustentaveis (descricao_projeto, custo_projeto, status_projeto, id_tipo_fonte, id_regiao)
            VALUES (:1, :2, :3, :4, :5)
            RETURNING id_projeto INTO :id_projeto
        """, [descricao, custo, status, id_tipo_fonte, id_comunidade], id_projeto=int)

        id_projeto = cursor.var(int).getvalue()

        cursor.execute("""
            INSERT INTO tb_comunidades_projetos (id_comunidade, id_projeto)
            VALUES (:1, :2)
        """, [id_comunidade, id_projeto])

        connection.conn.commit()
        print(f"Projeto '{descricao}' inserido e associado automaticamente à comunidade '{id_comunidade}'.")

    except Exception as e:
        print("Erro ao inserir projeto:", e)

# READ - Exibir Projeto Sustentável por ID
def exibir_projeto_por_id():
    try:
        id_projeto = validations.validar_numero("Digite o ID do projeto que deseja visualizar")
        if id_projeto is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_projeto, descricao_projeto, custo_projeto, status_projeto, id_tipo_fonte, id_regiao
            FROM tb_projetos_sustentaveis
            WHERE id_projeto = :1
        """, [id_projeto])
        projeto = cursor.fetchone()
        cursor.close()

        if projeto:
            print(f"""
            |=========== DETALHES DO PROJETO ===========|
            | ID do Projeto:        {projeto[0]:<8}       |
            | Descrição:            {projeto[1]:<15}       |
            | Custo:                {projeto[2]:<11.2f}    |
            | Status:               {projeto[3]:<12}       |
            | Tipo de Fonte ID:     {projeto[4]:<8}        |
            | Região ID:            {projeto[5]:<8}        |
            |===========================================|
            """)
        else:
            print("Nenhum projeto encontrado com o ID informado.")
    except Exception as e:
        print("Erro ao exibir projeto por ID:", e)

# READ - Exibir Todos os Projetos
def exibir_todos_projetos():
    try:
        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_projeto, descricao_projeto, custo_projeto, status_projeto, id_tipo_fonte, id_regiao
            FROM tb_projetos_sustentaveis
            ORDER BY id_projeto ASC
        """)
        projetos = cursor.fetchall()
        cursor.close()

        if projetos:
            print("| ID  | Descrição           | Custo       | Status       | Fonte ID | Região ID |")
            print("|-----|---------------------|-------------|--------------|----------|-----------|")
            for projeto in projetos:
                print(
                    f"| {projeto[0]:<4} | {projeto[1]:<19} | {projeto[2]:<11.2f} | {projeto[3]:<12} | {projeto[4]:<8} | {projeto[5]:<9} |")
        else:
            print("Nenhum projeto cadastrado.")

    except Exception as e:
        print("Erro ao exibir todos os projetos:", e)

# UPDATE - Alterar Projeto Sustentável
def alterar_projeto():
    try:
        cursor = connection.conn.cursor()

        id_projeto = validations.validar_numero("Digite o ID do projeto que deseja alterar")
        if id_projeto is None:
            return

        cursor.execute("""
            SELECT id_projeto, descricao_projeto, custo_projeto, status_projeto
            FROM tb_projetos_sustentaveis
            WHERE id_projeto = :1
        """, [id_projeto])
        projeto = cursor.fetchone()

        if not projeto:
            print("Nenhum projeto encontrado com o ID informado.")
            return

        print(
            f"Projeto encontrado: ID: {projeto[0]}, Descrição: {projeto[1]}, Custo: {projeto[2]}, Status: {projeto[3]}")

        descricao = validations.validar_texto("Nova descrição do projeto (ou deixe vazio para não alterar)",
                                              permitir_vazio=True)
        custo = validations.validar_numero("Novo custo do projeto (ou deixe vazio para não alterar)", tipo="float",
                                           permitir_vazio=True)

        status = None
        while True:
            print("Escolha o novo status do projeto (ou deixe vazio para não alterar):")
            print("[1] Em andamento")
            print("[2] Concluído")
            status_opcao = input("Digite o número correspondente ao status: ").strip()
            if not status_opcao:
                break
            if status_opcao in ["1", "2"]:
                status = "Em andamento" if status_opcao == "1" else "Concluído"
                break
            print("Opção inválida. Escolha '1' ou '2', ou deixe vazio para não alterar.")

        query = "UPDATE tb_projetos_sustentaveis SET "
        params = []

        if descricao:
            query += "descricao_projeto = :1, "
            params.append(descricao)
        if custo:
            query += "custo_projeto = :2, "
            params.append(custo)
        if status:
            query += "status_projeto = :3, "
            params.append(status)

        if not params:
            print("Nenhuma alteração foi feita.")
            return

        query = query.rstrip(", ")
        query += " WHERE id_projeto = :4"
        params.append(id_projeto)

        cursor.execute(query, params)
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Projeto alterado com sucesso!")
        else:
            print("Nenhuma alteração realizada.")
        cursor.close()

    except Exception as e:
        print("Erro ao alterar projeto:", e)

# DELETE - Excluir Projeto Sustentável
def excluir_projeto():
    try:
        id_projeto = validations.validar_numero("Digite o ID do projeto que deseja excluir")
        if id_projeto is None:
            return

        cursor = connection.conn.cursor()

        cursor.execute("""
            SELECT descricao_projeto
            FROM tb_projetos_sustentaveis
            WHERE id_projeto = :1
        """, [id_projeto])
        projeto = cursor.fetchone()

        if not projeto:
            print("Nenhum projeto encontrado com o ID informado.")
            return

        confirmacao = validations.validar_opcao(
            f"Tem certeza que deseja excluir o projeto '{projeto[0]}'? [S/N]",
            ["S", "N"]
        )
        if confirmacao == "N":
            print("Operação de exclusão cancelada.")
            return

        cursor.execute("""
            DELETE FROM tb_projetos_sustentaveis
            WHERE id_projeto = :1
        """, [id_projeto])
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Projeto excluído com sucesso!")
        else:
            print("Erro ao excluir o projeto. Nenhuma alteração realizada.")
        cursor.close()

    except Exception as e:
        print("Erro ao excluir projeto:", e)
