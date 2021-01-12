from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    print('------------------------------------')
    print('-------------Banco banco------------')
    print('------------------------------------')

    print('Selecione uma opção')
    print('1 - Abrir conta')
    print('2 - Sacar')
    print('3 - Depositar')
    print('4 - Transferir')
    print('5 - Listar contas')
    print('6 - Sair')

    opc:int = int(input())

    if opc == 1:
        criar_conta()
    elif opc == 2:
        sacar()
    elif opc == 3:
        depositar()
    elif opc == 4:
        transferir()
    elif opc == 5:
        listar_contas()
    elif opc == 6:
        print('volte sempre')
        sleep(2)
        exit(0)
    else:
        print('opção inválida')
        sleep(2)
        menu()
    

def criar_conta() -> None:
    print('Informe os dados do cliente:')

    nome:str = input('Nome do cliente')
    email:str = input('E-mail do cliente')
    cpf:str = input('Cpf do cliente')
    data_nasc: str = input('Data de nascimento')

    cliente: Cliente = Cliente(nome,email,cpf,data_nasc)

    conta: Conta(cliente)
    contas.append(conta)
    
    print('Conta criada com sucesso')
    print('Dados da conta')
    print('------------------------')
    print(conta)
    sleep(2)
    exit()

def sacar() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta'))
        conta: Conta = buscar_contas_por_numero(numero)

        if conta:
            valor:float = float(input('Informe o valor do saque'))

            conta.sacar(valor)
            
        else:
            print(f'Não foi encontrada conta com número: {numero}')

    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()

def depositar() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta'))

        conta: Conta = buscar_contas_por_numero(numero)

        if conta:
            valor:float = float(input('Informe o valor do depósito'))
            conta.depositar(valor)
        else:
            print(f'Naõ foi encontrada com conta {numero}')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()

def transferir() -> None:
    if len(contas) > 0:
        numero_origem:int = int(input('Infome o número da conta: '))
        conta_origem: Conta = buscar_contas_por_numero(numero_origem)

        if conta_origem:
            numero_destino:int = int(input('Informe a conta de destino: '))
            conta_d: Conta(buscar_contas_por_numero(numero_destino))

            if conta_d:
                valor: float = float(input('Informe o valor da transferencia: '))
                conta_origem.transferir(conta_d,valor)

            else:
                print(f'A conta destino {conta_d} não foi encontrada')
        
        else:
            print('Sua conta {numero_origem} não foi encontrada')

    else:
        print('Sem contas cadastradas')
    sleep(2)
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        for conta in contas:
            print(conta)
            print('-------------')
            sleep(1)
    else:
        print(f'Sem contas cadastradas')
    sleep(2)
    menu()

def buscar_contas_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c

if __name__ == "__main__":
    main()