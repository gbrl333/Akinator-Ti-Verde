import pandas as pd
from pkg_resources import yield_lines

dados = pd.read_csv('perguntas.csv')
piloto = None
v = []
while not piloto:

    perguntas = list(dados.columns[1:].values)
    respostas = []
   

    for pergunta in perguntas:
        respostas.append(dados[pergunta].sum())

    pergunta_rodada = perguntas[respostas.index(max(respostas))]
    resposta_rodada = input(f'{pergunta_rodada}(S para Sim / N para Não / NS para Nao sei)')

    if resposta_rodada == 'S':
        y = pergunta_rodada
        v.append(y)
        x = int(1)
        v.append(x)
        dados = dados[dados[pergunta_rodada] == 1].drop(columns=[pergunta_rodada])
    elif resposta_rodada =='N':
        y = pergunta_rodada
        v.append(y)
        x = int(0)
        v.append(x)
        dados = dados[dados[pergunta_rodada] == 0].drop(columns=[pergunta_rodada])
    elif resposta_rodada == 'SIM':
        dados = dados[dados[pergunta_rodada] == 1].drop(columns=[pergunta_rodada])
    elif resposta_rodada =='NAO':
        dados = dados[dados[pergunta_rodada] == 0].drop(columns=[pergunta_rodada])

    if len(dados.index) == 1:
        piloto = dados['Piloto'].values[0]
    elif len(dados.index) == 0:
        print('As Respostas foram Inconclusivas. Vamos Recomeçar?')
        dados = pd.read_csv('perguntas.csv')

       
print(f'A resposta é : {piloto}')

arquivo = open(input('Nome do arquivo a ser editado:'), 'r+')
texto = arquivo.readlines()
texto.append(input('insira o valor'))
arquivo.writelines(texto)
arquivo.close()