from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.crud.empresas import (
    inserir_empresa,
    exibir_empresa_por_id,
    exibir_todas_empresas,
    alterar_empresa,
    excluir_empresa,
)

# Definir o roteador
router = APIRouter()

# Modelos de entrada para as operações
class EmpresaInput(BaseModel):
    nome_empresa: str
    cnpj_empresa: str

class EmpresaUpdate(BaseModel):
    id_empresa: int
    nome_empresa: str = None
    cnpj_empresa: str = None

# Rota para criar uma nova empresa
@router.post("/empresas/")
def criar_empresa(empresa: EmpresaInput):
    try:
        inserir_empresa(empresa.nome_empresa, empresa.cnpj_empresa)
        return {"message": f"Empresa '{empresa.nome_empresa}' cadastrada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar empresa: {str(e)}")

# Rota para listar todas as empresas
@router.get("/empresas/")
def listar_empresas():
    try:
        empresas = exibir_todas_empresas()
        return {"empresas": empresas}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao listar empresas: {str(e)}")

# Rota para buscar uma empresa por ID
@router.get("/empresas/{empresa_id}")
def buscar_empresa(empresa_id: int):
    try:
        empresa = exibir_empresa_por_id(empresa_id)
        if not empresa:
            raise HTTPException(status_code=404, detail="Empresa não encontrada")
        return empresa
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao buscar empresa: {str(e)}")

# Rota para atualizar uma empresa
@router.put("/empresas/")
def atualizar_empresa(empresa: EmpresaUpdate):
    try:
        alterar_empresa(empresa.id_empresa, empresa.nome_empresa, empresa.cnpj_empresa)
        return {"message": "Empresa atualizada com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar empresa: {str(e)}")

# Rota para excluir uma empresa
@router.delete("/empresas/{empresa_id}")
def deletar_empresa(empresa_id: int):
    try:
        excluir_empresa(empresa_id)
        return {"message": "Empresa excluída com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao excluir empresa: {str(e)}")
