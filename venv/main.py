from fastapi import FastAPI, Query
import requests


app = FastAPI()

@app.get("/api/hello")
def hello_world():
    '''
    end point que exibe uma mensagem incrivel do mundo da programação!

    '''
    return {"message": "Hello World"}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    end point que lista os restaurantes e o cardapio de um determinado restaurante
    :param restaurante:
    :return:
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}


        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item" : item['Item'],
                    "price" : item['price'],
                    "description" : item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro na requisição': response.status_code - {response.text}}


