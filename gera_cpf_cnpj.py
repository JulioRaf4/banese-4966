import random

def calcular_digito(digitos, pesos):
    soma = sum(d * p for d, p in zip(digitos, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    for _ in range(2):
        cpf.append(calcular_digito(cpf, list(range(10, 1, -1))[:len(cpf)]))
    return ''.join(map(str, cpf))

def gerar_cnpj():
    cnpj = [random.randint(0, 9) for _ in range(8)] + [0, 0, 0, 1]
    for _ in range(2):
        cnpj.append(calcular_digito(cnpj, list(range(6, 1, -1)) + list(range(9, 1, -1))[:len(cnpj)]))
    return ''.join(map(str, cnpj))

def gerar_documento(tipo):
    """
    Gera um documento (CPF ou CNPJ) válido de forma aleatória.

    Args:
        tipo (str): O tipo do documento a ser gerado. Pode ser 'CPF' ou 'CNPJ'.

    Returns:
        str: Um CPF ou CNPJ válido, de acordo com o tipo especificado.
    """
    if tipo.upper() == 'CPF':
        return gerar_cpf()
    elif tipo.upper() == 'CNPJ':
        return gerar_cnpj()
    else:
        raise ValueError("Tipo inválido. Escolha 'CPF' ou 'CNPJ'.")

