from models.cliente import Cliente
from models.conta import Conta

Fábio: Cliente = Cliente('Fábio','fabio@gmail.com',12310923810923,'18/11/1990')
Camila: Cliente = Cliente('Camila','camil@gmail.com',12310923876,'01/01/1990')


contaf: Conta = Conta(Fábio)
contaPj: Conta = Conta(Camila)

print(contaf)
print(contaPj)