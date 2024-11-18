from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from typing import Optional
import cx_Oracle
import pandas as pd
from app.connection import conecta_banco  # Importa a função de conexão com o Oracle

router = APIRouter()

@router.get("/empresas/consulta")
async def consulta_empresas(
        nome_empresa: Optional[str] = Query(None, description="Filtrar por nome da empresa"),
        cnpj_empresa: Optional[str] = Query(None, description="Filtrar por CNPJ"),
        exportar: Optional[str] = Query(None, description="Formato de exportação: 'json' ou 'excel'")
):
    """
    Consulta empresas com filtros opcionais e permite exportar os dados.
    """
    conn = conecta_banco()  # Função para conectar ao banco
    cursor = conn.cursor()

    # Construir consulta dinâmica com filtros
    query = "SELECT * FROM tb_empresas WHERE 1=1"
    params = {}

    if nome_empresa:
        query += " AND nome_empresa LIKE :nome_empresa"
        params["nome_empresa"] = f"%{nome_empresa}%"  # Bind variable para Oracle

    if cnpj_empresa:
        query += " AND cnpj_empresa = :cnpj_empresa"
        params["cnpj_empresa"] = cnpj_empresa  # Bind variable para Oracle

    try:
        # Executar a consulta com os parâmetros
        cursor.execute(query, params)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
    except Exception as e:
        conn.close()
        return JSONResponse(content={"error": str(e)}, status_code=500)

    conn.close()

    # Converter resultados em um DataFrame
    df = pd.DataFrame(rows, columns=columns)

    # Exportar os dados, se solicitado
    if exportar == "json":
        return JSONResponse(content=df.to_dict(orient="records"))
    elif exportar == "excel":
        file_path = "empresas.xlsx"
        df.to_excel(file_path, index=False)
        return JSONResponse(content={"message": f"Arquivo exportado para {file_path}"})

    # Retornar os resultados como JSON
    return JSONResponse(content=df.to_dict(orient="records"))
