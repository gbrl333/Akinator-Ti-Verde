import PySimpleGUI as sg
import os
import time
import random
import sys
import pandas as pd
from pkg_resources import yield_lines


dados = pd.read_csv('perguntas.csv')
piloto = None
teste = 'igual'
v = []
#LAYOUT
def janela_inicial():
    layout = [
        [sg.Text('Texto Chatao de Apresentaçao')]
        [sg.Button('Começar')]
    ]




layout2 = [
    [sg.Text('My Layout')],
    [sg.Text('Pergunta:') , sg.Text(size=(20,1), key='-OUT-')],
    [sg.Input(key='-IN-')],
    [sg.Button('OK') , sg.Button('Cancel')]
  ]
#jANELA

janela = sg.Window('Tela inicial', layout)

while True:
    event , valores = janela.read()
    print(event,valores)
    perguntas = list(dados.columns[1:].values)
    respostas = []
   
    
    
    if event in (None ,'CANCEL'):
       break
    if event == 'OK':
       janela['-OUT-'].update(teste)
       resposta = valores['-IN-']
       print(resposta)
    



#AKINATOR


while not piloto:

    perguntas = list(dados.columns[1:].values)
    respostas = []
   

    for pergunta in perguntas:
        respostas.append(dados[pergunta].sum())

    pergunta_rodada = perguntas[respostas.index(max(respostas))]
    resposta_rodada = input(f'{pergunta_rodada}(S para Sim / N para Não )')

    if resposta_rodada == 'S' or resposta_rodada == 'SIM':
        y = pergunta_rodada
        v.append(y)
        x = ('sim')
        v.append(x)
        dados = dados[dados[pergunta_rodada] == 1].drop(columns=[pergunta_rodada])

    elif resposta_rodada =='N' or resposta_rodada =='NAO':
        y = pergunta_rodada
        v.append(y)
        x =('nao')
        v.append(x)
        dados = dados[dados[pergunta_rodada] == 0].drop(columns=[pergunta_rodada])
    else :
        print(f'input invalido')
        
   

    if len(dados.index) == 1:
        piloto = dados['Piloto'].values[0]
    elif len(dados.index) == 0:
        print('As Respostas foram Inconclusivas,Por favor Digite Sua Resposta:')
        info = v
        df = pd.DataFrame(info)
        df.to_csv(f'{input()}.txt')
        print('Resposta Salva Com sucesso')
        piloto = int(0)
        


       
print(f'A resposta é : {piloto}')
