"""
SOLARA

GRUPO
EcoMinds

INTEGRANTES
Adonay Rodrigues da Rocha | RM 558782
Marina Yumi Kanadani | RM 558404
Pedro Henrique Martins dos Reis | RM 555306
"""

from app import validations, connection

# CREATE - Inserir Empresa
def inserir_empresa():
    try:
        nome_empresa = validations.validar_texto("Digite o nome da empresa")
        if nome_empresa is None:
            return

        while True:
            cnpj_empresa = validations.validar_texto("Digite o CNPJ da empresa (somente números)")
            if cnpj_empresa is None:
                return

            if len(cnpj_empresa) != 14 or not cnpj_empresa.isdigit():
                print("CNPJ inválido. Certifique-se de que possui 14 dígitos numéricos.")
                continue

            break

        cursor = connection.conn.cursor()
        cursor.execute("""
            INSERT INTO tb_empresas (nome_empresa, cnpj_empresa)
            VALUES (:1, :2)
        """, [nome_empresa, cnpj_empresa])
        connection.conn.commit()
        print(f"Empresa '{nome_empresa}' cadastrada com sucesso!")
        cursor.close()

    except Exception as e:
        print("Erro ao cadastrar empresa:", e)

# READ - Exibir Empresa por ID
def exibir_empresa_por_id():
    try:
        id_empresa = validations.validar_numero("Digite o ID da empresa")
        if id_empresa is None:
            return

        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_empresa, nome_empresa, cnpj_empresa
            FROM tb_empresas
            WHERE id_empresa = :1
        """, [id_empresa])
        empresa = cursor.fetchone()
        cursor.close()

        if empresa:
            print(f"ID: {empresa[0]}, Nome: {empresa[1]}, CNPJ: {empresa[2]}")
        else:
            print("Nenhuma empresa encontrada com o ID informado.")

    except Exception as e:
        print("Erro ao buscar a empresa:", e)

# READ - Exibir Todas as Empresas
def exibir_todas_empresas():
    try:
        cursor = connection.conn.cursor()
        cursor.execute("""
            SELECT id_empresa, nome_empresa, cnpj_empresa
            FROM tb_empresas
            ORDER BY id_empresa ASC
        """)
        empresas = cursor.fetchall()
        cursor.close()

        if empresas:
            print("| ID  | Nome da Empresa           | CNPJ         |")
            print("|-----|---------------------------|--------------|")
            for empresa in empresas:
                print(f"| {empresa[0]:<4} | {empresa[1]:<25} | {empresa[2]:<12} |")
        else:
            print("Nenhuma empresa cadastrada.")

    except Exception as e:
        print("Erro ao exibir empresas:", e)

# UPDATE - Alterar Empresa
def alterar_empresa():
    try:
        id_empresa = validations.validar_numero("Digite o ID da empresa que deseja alterar")
        if id_empresa is None:
            return

        cursor = connection.conn.cursor()

        # Verificar se a empresa existe
        cursor.execute("""
            SELECT id_empresa, nome_empresa, cnpj_empresa
            FROM tb_empresas
            WHERE id_empresa = :1
        """, [id_empresa])
        empresa = cursor.fetchone()

        if not empresa:
            print("Nenhuma empresa encontrada com o ID informado.")
            return

        print(f"Empresa encontrada: ID: {empresa[0]}, Nome: {empresa[1]}, CNPJ: {empresa[2]}")

        # Solicitar novas informações
        novo_nome = validations.validar_texto("Novo nome da empresa (ou deixe vazio para não alterar)",
                                              permitir_vazio=True)
        novo_cnpj = None

        while True:
            novo_cnpj = validations.validar_texto("Novo CNPJ da empresa (ou deixe vazio para não alterar)",
                                                  permitir_vazio=True)
            if not novo_cnpj:
                break
            if len(novo_cnpj) == 14 and novo_cnpj.isdigit():
                break
            print("CNPJ inválido. Certifique-se de que possui 14 dígitos numéricos.")

        # Montar a query dinamicamente
        query = "UPDATE tb_empresas SET "
        params = []

        if novo_nome:
            query += "nome_empresa = :1, "
            params.append(novo_nome)
        if novo_cnpj:
            query += "cnpj_empresa = :2, "
            params.append(novo_cnpj)

        if not params:
            print("Nenhuma alteração foi feita.")
            return

        query = query.rstrip(", ")  # Remove a vírgula final
        query += " WHERE id_empresa = :3"
        params.append(id_empresa)

        # Executar a query
        cursor.execute(query, params)
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Empresa alterada com sucesso!")
        else:
            print("Nenhuma alteração realizada.")
        cursor.close()

    except Exception as e:
        print("Erro ao alterar a empresa:", e)

# DELETE - Excluir Empresa
def excluir_empresa():
    try:
        id_empresa = validations.validar_numero("Digite o ID da empresa que deseja excluir")
        if id_empresa is None:
            return

        cursor = connection.conn.cursor()

        # Verificar dependências
        cursor.execute("""
            SELECT COUNT(*)
            FROM tb_comunidades
            WHERE id_empresa = :1
        """, [id_empresa])
        dependencias = cursor.fetchone()[0]

        if dependencias > 0:
            print(
                f"Não é possível excluir a empresa com ID {id_empresa} porque ela está associada a {dependencias} comunidade(s).")
            return

        # Confirmar exclusão
        cursor.execute("""
            SELECT nome_empresa
            FROM tb_empresas
            WHERE id_empresa = :1
        """, [id_empresa])
        empresa = cursor.fetchone()

        if not empresa:
            print("Nenhuma empresa encontrada com o ID informado.")
            return

        confirmacao = validations.validar_opcao(
            f"Tem certeza que deseja excluir a empresa '{empresa[0]}'? [S/N]",
            ["S", "N"]
        )
        if confirmacao == "N":
            print("Operação de exclusão cancelada.")
            return

        # Excluir a empresa
        cursor.execute("""
            DELETE FROM tb_empresas
            WHERE id_empresa = :1
        """, [id_empresa])
        connection.conn.commit()

        if cursor.rowcount > 0:
            print("Empresa excluída com sucesso!")
        else:
            print("Erro ao excluir a empresa.")
        cursor.close()

    except Exception as e:
        print("Erro ao excluir a empresa:", e)
