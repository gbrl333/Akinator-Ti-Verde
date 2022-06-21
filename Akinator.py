import PySimpleGUI as sg
import os
import time
import random
import sys
import pandas as pd
from pkg_resources import yield_lines


dados = pd.read_csv('pergunta.csv')
piloto = None
v = []

#LAYOUT
def janela_inicial():
    layout = [
        [sg.Text('Comece pensando em um objeto e descreva-o,',size=(100,1),background_color='#538A42')],
        [sg.Text('nossa inteligência artificial adivinhará o que estava pensando e lhe daremos formas de reciclá-lo, se possível.',size=(100,1),background_color='#538A42')],
        [sg.Text('Caso não acerte pedimos que colabore com nosso banco de dados e diga em que estava pensando!',size=(100,1),background_color='#538A42')],
        [sg.Text('Agora que você já sabe como o jogo funciona, que tal jogarmos um pouquinho?',size=(100,1),background_color='#538A42')],
        [sg.Text('',background_color='#538A42')],
        [sg.Button('Começar',size=(100,1),button_color=('#416536'))]
        
        
    ]
    
    return sg.Window('Login',layout= layout,background_color='#538A42',grab_anywhere=True,finalize=True,auto_size_text=True,size=(800,200))
def janela_dois():
    layout = [
        [sg.Text('Pergunta:',background_color='#538A42') , sg.Text(size=(20,1), key='PERGUNTA',background_color='#538A42')],
        [sg.Text('(SIM ou NAO)',background_color='#538A42')],
        [sg.Input(key='Resposta',do_not_clear=False)],
        [sg.Button('Enviar',button_color=('#416536')) , sg.Button('Cancel',button_color=('#416536'))]
    ]
    return sg.Window('Perguntas', layout=layout,finalize=True,keep_on_top=True,auto_size_text=True,background_color='#538A42')

def janela_tres():
    layout = [
        [sg.Text('Sua Resposta é',background_color='#538A42')],
        [sg.Text(size=(20,1),key='RESPOSTAF',background_color='#538A42')]

    ]
    return sg.Window('Resposta', layout=layout,finalize=True,keep_on_top=True,background_color='#538A42')

def janela_quatro():
    layout = [
        [sg.Text('Sua Resposta Foi Inconclusiva')],
        [sg.Text('Digite sua Resposta para Salvarmos no Banco de Dados ')],
        [sg.Input(key='Arquivo')],
        [sg.Button('Enviar para o Banco')]

    ]
    return sg.Window('Resposta', layout=layout,finalize=True,keep_on_top=True)

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
            piloto = dados['Material'].values[0]
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
        
        

        


 