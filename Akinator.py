import PySimpleGUI as sg
import os
import time
import random
import sys
import pandas as pd
from pkg_resources import yield_lines


dados = pd.read_csv('perguntas.csv')
piloto = None
v = []

#LAYOUT
def janela_inicial():
    layout = [
        [sg.Text('Texto Chatao de Apresentaçao')],
        [sg.Button('Começar')]
    ]
    return sg.Window('Login',layout= layout,finalize=True)
def janela_dois():
    layout = [
        [sg.Text('My Layout')],
        [sg.Text('Pergunta:') , sg.Text(size=(20,1), key='PERGUNTA')],
        [sg.Input(key='Resposta',do_not_clear=False)],
        [sg.Button('Enviar') , sg.Button('Cancel')]
    ]
    return sg.Window('dois', layout=layout,finalize=True,keep_on_top=True)

def janela_tres():
    layout = [
        [sg.Text('Sua Resposta é')],
        [sg.Text(size=(20,1),key='RESPOSTAF')]

    ]
    return sg.Window('tres', layout=layout,finalize=True,keep_on_top=True)

def janela_quatro():
    layout = [
        [sg.Text('Sua Resposta Foi Inconclusiva')],
        [sg.Text('Digite sua Resposta para Salvarmos no Banco de Dados ')],
        [sg.Input(key='Arquivo')],
        [sg.Button('Enviar para o Banco')]

    ]
    return sg.Window('tres', layout=layout,finalize=True,keep_on_top=True)

#JANELA

janela1,janela2,janela3,janela4 =janela_inicial(),None,None,None


#FUNCIONAMENTO 

while True:
    window , event , valores = sg.read_all_windows()
    perguntas = list(dados.columns[1:].values)
    respostas = []
    

    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela2 and event == sg.WIN_CLOSED:
        break

    if window == janela3 and event == sg.WIN_CLOSED:
            break

    if window == janela4 and event == sg.WIN_CLOSED:
            break

    if piloto != None :
        print('oi')
        janela3 = janela_tres()
        janela2.hide()
        janela3['RESPOSTAF'].update(piloto)
    
    if piloto == 0 :
        janela4 = janela_quatro()
        janela2.hide()
        
        
        

    for pergunta in perguntas:
        respostas.append(dados[pergunta].sum())
        pergunta_rodada = perguntas[respostas.index(max(respostas))]
        
     

    if window == janela1 and event == 'Começar':
        janela2 = janela_dois()
        janela1.hide()
        janela2['PERGUNTA'].update(pergunta_rodada)
    
       
   
    if window == janela2:
        
        print('')

    if window == janela2 and event == 'Enviar':
        
         
        resposta_rodada = valores['Resposta']
        
        if resposta_rodada == 'S' or resposta_rodada == 'SIM':
            y = pergunta_rodada
            v.append(y)
            x = ('sim')
            v.append(x)
            dados = dados[dados[pergunta_rodada] == 1].drop(columns=[pergunta_rodada])
            print('s')
            

        elif resposta_rodada =='N' or resposta_rodada =='NAO':
            y = pergunta_rodada
            v.append(y)
            x =('nao')
            v.append(x)
            dados = dados[dados[pergunta_rodada] == 0].drop(columns=[pergunta_rodada])
            print('n')
            
        else :
            print(f'input invalido')

    if len(dados.index) == 1:
            piloto = dados['Piloto'].values[0]
            info = v
            df = pd.DataFrame(info)
            df.to_csv(f'TESTE1.txt')
            print('Resposta Salva Com sucesso')  
            

    elif len(dados.index) == 0:
            print('As Respostas foram Inconclusivas,Por favor Digite Sua Resposta:')
            piloto = int(0)
            info = v
            df = pd.DataFrame(info)
            df.to_csv(f'TESTE.txt')
            print('Resposta Salva Com sucesso')        

        
    janela2['PERGUNTA'].update(pergunta_rodada)
        
        

        


 