"""
SOLARA

GRUPO
EcoMinds

INTEGRANTES
Adonay Rodrigues da Rocha | RM 558782
Marina Yumi Kanadani | RM 558404
Pedro Henrique Martins dos Reis | RM 555306
"""

import cx_Oracle

def conecta_banco():

    try:
        user = "rm558404"
        password = "090790"
        dsn = cx_Oracle.makedsn(
            host="oracle.fiap.com.br",
            port=1521,
            service_name="ORCL"
        )

        conn = cx_Oracle.connect(
            user=user,
            password=password,
            dsn=dsn
        )
        return conn
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

conn = conecta_banco()
