"""
Codigo apenas para saber o valor das horas passando mais rapido
"""

# importando biblioteca datetime para convesao de horas, minutos e segundos
import datetime
# from PySimpleGUI import PySimpleGUI as sg

# Variaveis que estao recebendo os valores das horas a serem calculadas
horas = float(input("Informe as horas: "))
vezes = float(input("Quantas vezes ela foi acelerada: "))

# Layout
"""sg.theme('DarkBlue14')

layout = [
    [sg.Number('Horas'), sg.Input(key=horas)],
    [sg.Number('Vezes'), sg.Input(key=vezes)],
    [sg.Button('Calcular')]
]"""


# Janela
# Ler os eventos

# Transformando as horas informadas em minutos
def mult_hora():
    min_horas = horas * 60
    min_total = min_horas / vezes
    horas_total = min_total / 60
    print(f"O tempo restante é de: {str(datetime.timedelta(minutes=horas_total))}.")


# Chamando a funcao criada para mulriplicar as horas

mult_hora()
