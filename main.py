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
    resposta_rodada = input(f'{pergunta_rodada}(S para Sim / N para Não ')

    if resposta_rodada == 'S':
        y = pergunta_rodada
        v.append(y)
        x = ('sim')
        v.append(x)
        dados = dados[dados[pergunta_rodada] == 1].drop(columns=[pergunta_rodada])
    elif resposta_rodada =='N':
        y = pergunta_rodada
        v.append(y)
        x =('nao')
        v.append(x)
        dados = dados[dados[pergunta_rodada] == 0].drop(columns=[pergunta_rodada])
    elif resposta_rodada == 'SIM':
        y = pergunta_rodada
        v.append(y)
        x = ('sim')
        v.append(x)
        dados = dados[dados[pergunta_rodada] == 1].drop(columns=[pergunta_rodada])
    elif resposta_rodada =='NAO':
        y = pergunta_rodada
        v.append(y)
        x =('nao')
        v.append(x)
        dados = dados[dados[pergunta_rodada] == 0].drop(columns=[pergunta_rodada])

    if len(dados.index) == 1:
        piloto = dados['Piloto'].values[0]
    elif len(dados.index) == 0:
        print('As Respostas foram Inconclusivas,Por favor Digite Sua Resposta:')
        info = v
        df = pd.DataFrame(info)
        df.to_csv(f'{input()}.txt')
        print('Resposta Salva Com sucesso')
        
        break


       
print(f'A resposta é : {piloto}')
