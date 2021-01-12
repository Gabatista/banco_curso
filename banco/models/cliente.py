from datetime import date
from utils.helper import date_para_str, str_para_date

class Cliente:
    contador: int = 10;

    def __init__(self:object, nome:str, email:str, cpf:str, data_nasc: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__cpf: int = cpf
        self.__email: str = email
        self.__data_nasc: date = str_para_date(data_nasc)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self:object) -> int:
        return self.__codigo

    @property
    def nome(self:object) -> str:
        return self.__nome

    @property
    def email(self:object) -> str:
        return self.__email

    @property
    def cpf(self:object) -> int:
        return self.__cpf

    @property
    def data_nasc(self:object) -> date:
        return self.__data_nasc

    @property
    def __data_cadastro(self:object) -> date:
        return self.__data_cadastro

    def __str__(self:object) -> str:
        return f'Código {self.codigo} \nNome: {self.nome} \nData de nascimento: {self.data_nasc} \nCadastro: {self.__data_cadastro}'

    