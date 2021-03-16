import random
from time import sleep
import math
import datetime
print("\033[7;33;40m-=-" * 54)
jo = ("\033[7;33;40m LOJA")
print(jo.center(170))
print("\033[7;33;40m-=-" * 54)
#----------------------------------------------------------------------------------------------------------------------

produto = int(input("Digite o valor do produto: "))
print("""Selecione a opção de pagamento:
[ 1 ] pagamento a vista 10% de desconto
[ 2 ] pagamento a vista no cartão 5% de desconto
[ 3 ] pagamento em 2x no cartão valor original
[ 4 ] pagamento em 3x no cartão 20% de juros""")
op = int(input("Digite a opção :"))
if(op == 1):
    valor = (produto*10)/100
    total = produto - valor
    print("TOTAL: R${}".format(total))
elif(op == 2):
    valor = (produto*5)/100
    total = produto - valor
    print("TOTAL: R${}".format(total))
elif(op == 3):
    valor = produto
    total = valor / 2
    print("TOTAL R${}".format(total))
elif(op == 4):
    valor = (produto*20)/100
    total = produto + valor
    div = total / 3
    print("TOTAL: R${} | 3x = R${}".format(total, div))
else:
    print("Valor invalido, tente novamente.")