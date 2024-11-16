'''
SOLARA

GRUPO
EcoMinds

INTEGRANTES
Adonay Rodrigues da Rocha | RM 558782
Marina Yumi Kanadani | RM 558404
Pedro Henrique Martins dos Reis | RM 555306
'''

import cx_Oracle

# Atribuindo valores às variáveis de conexão
user = "rm558404"
password = "090790"

# Montando o DSN
dsn = cx_Oracle.makedsn(
    host = "oracle.fiap.com.br",
    port = 1521,
    service_name = "ORCL"
)

# Conectando ao banco de dados Oracle
conn = cx_Oracle.connect(
    user="rm558404",
    password="090790",
    dsn="oracle.fiap.com.br:1521/orcl"
)