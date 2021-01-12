from datetime import date
from datetime import datetime

def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%y')

def str_para_date(data: str) -> date:
    return datetime.strftime(data, '%d/%m/%y')


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'