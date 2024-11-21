import base64
import hashlib
import random

from app.connection import conn

empresas_reais = [
    {
        "razao_social": "EcoMinds Ltda.",
        "cnpj": "12345678901234",
        "imagem": "https://drive.google.com/file/d/1sfh4RLeR0_T7uoWrww92Rxbi7idLHw4n/view?usp=drive_link",
        "descricao": "Empresa que busca inovar na promoção de energia limpa e acessível a todos os brasileiros."
    },
    {
        "razao_social": "Atvos Bioenergia Brenco S.A.",
        "cnpj": "08070566002900",
        "imagem": "https://drive.google.com/file/d/17p0Ye3yS-ByJ1tO-JRXTSzJPo5x3AUUc/view?usp=drive_link",
        "descricao": "Uma das pioneiras em bioenergia no Brasil."
    },
    {
        "razao_social": "Siemens Gamesa Energia Renovável LTDA.",
        "cnpj": "69119386001719",
        "imagem": "https://drive.google.com/file/d/1rhBc7kQOioC0MJw1WMPhBImZRexgzBa0/view?usp=drive_link",
        "descricao": "Especialista global em energia eólica e sustentável."
    },
    {
        "razao_social": "Engie Energia Solar S.A.",
        "cnpj": "24743728000171",
        "imagem": "https://drive.google.com/file/d/1hB7PrpAqm8K4SkvKebiPVWBjmN8-Ke8g/view?usp=drive_link",
        "descricao": "Referência em soluções de energia solar no Brasil."
    },
    {
        "razao_social": "CPFL Energia S.A.",
        "cnpj": "08439659001394",
        "imagem": "https://drive.google.com/file/d/1LAU7nZoWLk9xOUID26WX2e59A0bTAzAp/view?usp=drive_link",
        "descricao": "Uma das maiores empresas de energia renovável no país."
    },
    {
        "razao_social": "Alupar Investimento S.A.",
        "cnpj": "08364948000138",
        "imagem": "https://drive.google.com/file/d/17p0Ye3yS-ByJ1tO-JRXTSzJPo5x3AUUc/view?usp=drive_link",
        "descricao": "Atua no desenvolvimento e operação de projetos de geração de energia renovável e transmissão de energia elétrica no Brasil e América Latina."
    },
    {
        "razao_social": "Serena Energia S.A.",
        "cnpj": "42500384000151",
        "imagem": "https://drive.google.com/file/d/1BvEeAob_Nc0qhDkr6ksfWp4PJ5ZSD7j7/view?usp=drive_link",
        "descricao": "Inovação em energia eólica e solar."
    },
    {
        "razao_social": "EDP Renováveis BrasilS.A.",
        "cnpj": "09334083000120",
        "imagem": "https://drive.google.com/file/d/1DpFn05P9RGfXIeNsmL6lpnA4Ktuul8p_/view?usp=drive_link",
        "descricao": "Especialista em soluções de energia renovável sustentável."
    },
    {
        "razao_social": "Statkraft Energias Renováveis S.A.",
        "cnpj": "00622416000141",
        "imagem": "https://drive.google.com/file/d/1QJt6Z3Py98_MI24PoOSGeV6mjAdo_jki/view?usp=drive_link",
        "descricao": "Líder europeia com forte atuação no Brasil."
    },
    {
        "razao_social": "Ibitu Energia S.A.",
        "cnpj": "31908280000164",
        "imagem": "https://drive.google.com/file/d/1VBzSCjlyBLa7Bd6Z82bC0HhyHl38nGyl/view?usp=drive_link",
        "descricao": "Referência em energia eólica e hidrelétrica no Brasil."
    },
    {
        "razao_social": "Elera Renováveis S.A.",
        "cnpj": "02808298000196",
        "imagem": "https://drive.google.com/file/d/1-1Henu9TzZ_oeipeBvuiVPA7g-aGxwLF/view?usp=drive_link",
        "descricao": "Uma das maiores geradoras de energia limpa no Brasil."
    },
    {
        "razao_social": "Casa dos Ventos Energias Renováveis S.A.",
        "cnpj": "10772867001433",
        "imagem": "https://drive.google.com/file/d/1MzF2vWZCmistRpDJO0dCmwtzo6YJ_p7Z/view?usp=drive_link",
        "descricao": "Empresa especializada em energia eólica com foco no sul do Brasil."
    },
    {
        "razao_social": "Neoenergia Renováveis Ltda.",
        "cnpj": "12227426000161",
        "imagem": "https://drive.google.com/file/d/10BX9YO_L1zJgQ3swM68aiBUwtrCmn5Qv/view?usp=drive_link",
        "descricao": "Uma das maiores empresas de energia renovável no Brasil, com foco em energia solar e eólica."
    },
    {
        "razao_social": "Solatio Energy Gestão de Projetos Solares Ltda.",
        "cnpj": "30418722000121",
        "imagem": "https://drive.google.com/file/d/1bgan8Ry8DHiUIa17z9PNl5xVuxBHjk7t/view?usp=drive_link",
        "descricao": "Referência no mercado de energia solar no Brasil, com projetos inovadores e sustentáveis."
    },
    {
        "razao_social": "Jirau Energia S.A.",
        "cnpj": "09029666000490",
        "imagem": "https://drive.google.com/file/d/1B-fFa2894Az9jsCFLCFwUqA6jv3S2Hmn/view?usp=drive_link",
        "descricao": "Atua na geração de energia sustentável por meio de hidrelétricas e energia solar."
    },
    {
        "razao_social": "Renova Energia S.A.",
        "cnpj": "08534605000255",
        "imagem": "https://drive.google.com/file/d/1_W-EJy381cNz4x412EhGjx_xkOJE7BOw/view?usp=drive_link",
        "descricao": "Empresa focada em geração de energia limpa, com projetos solares e eólicos em todo o Brasil."
    },
    {
        "razao_social": "Voltalia Energia do Brasil Ltda.",
        "cnpj": "08351042000340",
        "imagem": "https://drive.google.com/file/d/1hpM2KZxAXCONqwJ_WzECWQRElH2TEJiE/view?usp=drive_link",
        "descricao": "Atua globalmente no setor de energia renovável, com forte presença no Brasil em projetos solares."
    },
    {
        "razao_social": "Votorantim Energia S.A.",
        "cnpj": "23056547000104",
        "imagem": "https://drive.google.com/file/d/1i3-iRwTTFMFRt3eaJmgxfxmgp1Z7P4y5/view?usp=drive_link",
        "descricao": "Parte do grupo Votorantim, investe em projetos de energia renovável, incluindo eólica e solar."
    },
    {
        "razao_social": "Enel Green Power Cachoeira Dourada S.A. CDSA",
        "cnpj": "01672223000320",
        "imagem": "https://drive.google.com/file/d/1kQtckGT2Eiy3oO0v8kE8W0-2sttswZxc/view?usp=drive_link",
        "descricao": "Líder global em energias renováveis, atuando no Brasil com projetos de energia solar, eólica e hidrelétrica."
    },
    {
        "razao_social": "Raízen Energia S.A.",
        "cnpj": "08070508015876",
        "imagem": "https://drive.google.com/file/d/1aZPfvRT9CMvrh0Z0fkkFfJF5Orbpstah/view?usp=drive_link",
        "descricao": "Empresa integrada de energia, atuando na produção de etanol, bioeletricidade e distribuição de combustíveis."
    },
    {
        "razao_social": "Aurora Energia S.A.",
        "cnpj": "46205411000114",
        "imagem": "https://drive.google.com/file/d/1VXLw8ntrR61sVld6-T2aPZzhgX_9eUet/view?usp=drive_link",
        "descricao": "Especialista em soluções solares distribuídas, com forte atuação em comunidades remotas e projetos sustentáveis."
    }
]

# Função para gerar hash SHA-256 e base64 para senhas
def gerar_hash_sha256(senha):
    hash_object = hashlib.sha256(senha.encode('utf-8'))
    hash_base64 = base64.b64encode(hash_object.digest()).decode('utf-8')
    return hash_base64


# Função para inserir empresas na tabela tb_empresas
def inserir_empresas(empresas):
    try:
        cursor = conn.cursor()

        for empresa in empresas:
            razao_social = empresa["razao_social"]
            cnpj = empresa["cnpj"]

            # Verifica se é a empresa EcoMinds Ltda.
            if razao_social == "EcoMinds Ltda.":
                senha_clara = "ecominds123"  # Define uma senha fixa sem criptografia para testes
                senha_para_inserir = senha_clara  # Mantém a senha sem criptografar
            else:
                senha_clara = "".join(
                    random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*", k=8))
                senha_para_inserir = gerar_hash_sha256(senha_clara)  # Gera a senha hash para outras empresas

            imagem = empresa["imagem"]
            descricao = empresa["descricao"]

            # Insere os dados na tabela tb_empresas
            cursor.execute("""
                INSERT INTO tb_empresas (razao_social_empresa, cnpj_empresa, senha_empresa, imagem_empresa, descricao_empresa)
                VALUES (:1, :2, :3, :4, :5)
            """, (razao_social, cnpj, senha_para_inserir, imagem, descricao))

        conn.commit()
        print(f"{len(empresas)} empresas inseridas com sucesso.")
        cursor.close()

    except Exception as e:
        print(f"Erro ao inserir empresas reais: {e}")
