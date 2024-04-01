import json
import random
from gera_cpf_cnpj import gerar_documento
from gera_data import gerar_data_aleatoria

# Definição para gerar um dado conforme especificado
def gerar_dado():
    return {
        "numeroContrato": str(random.randint(0, 9999)),
        "eventos": random.choice(["LIBERACAO", "ATUALIZACAO", "AMORTIZACAO_LIQUIDACAO", "ATRASO", "RENEGOCIACAO", "ESTORNO"]),
        "tipoPessoa": random.choice(["F", "J"]),
        "numeroIdentificacaoPessoa": gerar_documento(random.choice(["CPF", "CNPJ"])), # Código de pessoa (CPF ou CNPJ) // criar uma função para gerar CNPJ Também
        "codigoEmpresa": random.randint(1, 4),
        "siglaSistema": random.choice(["SCC", "SCI", "SCCI", "CCO", "MCF", "ADC", "CYBERCORE"]),
        "codigoProduto": str(random.randint(0, 9999)), 
        "codigoSubProduto": str(random.randint(0, 9999)),
        "agencia": str(random.randint(0, 100)), #max 100
        "valorContratado": round(random.uniform(0.00, 99999.99), 2),
        "valorSaldoClassificado": round(random.uniform(0.00, 99999999.99), 2),
        "valorSaldoContabilBruto": round(random.uniform(0.00, 99999999.99), 2),
        "valorEntrada": round(random.uniform(0.00, 99999999.99), 2),
        "taxaJuros": round(random.uniform(0.01, 1.00), 2),
        "taxaJurosEfetivo": round(random.uniform(0.01, 0.10), 2),
        "contratosLiquidados": None, # lista de strings (talvez um campo na interface pra ele inserir as str)
        "dataInicioAtraso": None, # Data
        "dataContratacao": gerar_data_aleatoria("2024-01-01", "2030-12-31"), # Data
        "dataReferencia": gerar_data_aleatoria("2024-01-01", "2030-12-31"), # Data
        "dataVencimento": gerar_data_aleatoria("2024-01-01", "2030-12-31"), # Data
        # AS PARCELAS TAMBÉM TEM REGRA
        "parcelas": [
            {
                "numeroOrdem": 1,
                "dataVencimento": gerar_data_aleatoria("2024-01-01", "2030-12-31"), # Data
                "statusPagamento": random.choice(["FECHADA", "AMORTIZADA_PARCIALMENTE", "ABERTA"]),
                "dataPagamento": gerar_data_aleatoria("2024-01-01", "2030-12-31"), # Data
            },
            {
                "numeroOrdem": 2,
                "dataVencimento": gerar_data_aleatoria("2024-01-01", "2030-12-31"), # Data
                "statusPagamento": random.choice(["FECHADA", "AMORTIZADA_PARCIALMENTE", "ABERTA"]),
                "dataPagamento": gerar_data_aleatoria("2024-01-01", "2030-12-31"), # Data
            }
        ]
    }

# Gerar 50 dados
dados = [gerar_dado() for _ in range(10)]

# Salvar os dados em um arquivo de texto no formato JSON
caminho_arquivo = "./norma_4966/dados_contrato.json"

with open(caminho_arquivo, "w") as arquivo:
    json.dump(dados, arquivo, indent=4)

