import time

import requests
import json

class RequestData:
    def __init__(self):
        self.req = requests.Session()


    def run(self):
        for id in range(1,100):
            data = self.req.get(f'http://challenge.dienekes.com.br/api/numbers?page={id}')
            json_content = data.json()
            if json_content:
                if 'numbers' not in json_content.keys():
                    print("Query error, ID ", id)
                    continue

                numeros = json_content['numbers']

                lista = self.ordenar(numeros)
                print(lista)
            else:
                break

    def ordenar(self, lista):
        listaOrdenada = []
        x = 0
        lowest = lista[0]
        print("Antes = ", lista)
        while len(lista) > 0:
            if lista[x] < lowest:
                lowest = lista[x]
            x += 1
            if x == len(lista):
                listaOrdenada.append(lowest)
                lista.remove(lowest)
                if lista:
                    lowest = lista[0]
                x = 0

        print("Depois = ", listaOrdenada)
        return listaOrdenada




app = RequestData()
app.run()