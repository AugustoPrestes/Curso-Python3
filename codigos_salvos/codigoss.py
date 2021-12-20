# Codigo que gera valor randomico versao cara ou coroa.

from random import random


def joga_moeda():
    """ Funcao que determina , cara ou coroa. se o valor gerado aleatoriamento for maior que 0.5, a funcao retorna "cara", caso contrario, retorna "Coroa"  """
    if random() > 0.4999:
        return 'Cara'
    return 'Coroa'


def impar():  # Codigo Para verificar se valor corresponde a impar:
    numero = int(input('O seu valor e impar? '))
    if numero % 2 != 0:
        print('Sim')
    else:
        print('Nao')


def par():  # Codigo Para verificar se valor corresponde a par:
    numero = int(input('O seu valor e par? '))
    if numero % 2 != 0:
        print('nao')
    else:
        print('sim')


# Tela Para confrirmar valor entre par e impar
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('!Informe Qual verificação devemos fazer!')
print('!!!!!!!!!! opção: i para impar !!!!!!!!!!')
print('!!!!!!!!!!! opção: p para par !!!!!!!!!!!')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

opcao = input()

if opcao == 'i':
    impar()
if opcao == 'p':
    par()
# FIM de Tela Para confrirmar valor entre par e impar


# Funcao de raiz:
# Funcao para saber qual e a raiz quadrada do mesmo, ou qualquer outra raiz.
def func_raiz(numero, raiz=2):
    return numero ** raiz


# Funcao de exponencial:
# tetermina o valor da potencia do numero informado.
def func_potencia(numero, expoente=10):
    return numero ** expoente


# A baixo funcoes para calculadora
def soma():  # Funcao que soma dois valores.
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print("Resultado soma: ", a + b)


def divisao(a):  # Funcao que divide dois valores
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print("Resultado divisão: ", a % b)


def subtracao():  # Funcao que subtrai entre dois valores.
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print("Resultado subtração: ", a - b)


def multiplicacao():  # Funcao que multiplica doi valores.
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print("Resultado multiplicação: ", a * b)


while opcao:
    print("####################")
    print("# 0. Sair          #")
    print("# 1. Somar         #")
    print("# 2. Subtrair      #")
    print("# 3. Multiplicação #")
    print("# 4. Divisão       #")
    print("####################")

    opcao = int(input("Opção: "))

    if(opcao == 1):
        soma()
    if(opcao == 2):
        subtracao()
    if(opcao == 3):
        multiplicacao()
    if(opcao == 4):
        divisao()
