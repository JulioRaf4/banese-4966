from datetime import datetime, timedelta
import random

def gerar_data_aleatoria(data_inicio, data_fim):
    """
    Gera uma data aleatória dentro de um intervalo especificado.

    Args:
        data_inicio (str): A data de início do intervalo, no formato 'AAAA-MM-DD'.
        data_fim (str): A data de fim do intervalo, no formato 'AAAA-MM-DD'.

    Returns:
        str: Uma data aleatória dentro do intervalo especificado, no formato 'AAAA-MM-DD'.
    """
    inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
    fim = datetime.strptime(data_fim, "%Y-%m-%d")

    # Calcula a diferença entre as datas e gera um número aleatório de dias dentro desse intervalo
    diferenca_dias = (fim - inicio).days
    dias_aleatorios = random.randint(0, diferenca_dias)

    # Calcula a data aleatória
    data_aleatoria = inicio + timedelta(days=dias_aleatorios)

    return data_aleatoria.strftime("%Y-%m-%d")

