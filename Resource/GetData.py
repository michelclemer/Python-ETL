import asyncio
import time
import aiohttp
from aiohttp.client import ClientSession


class ColetarDados:
    def __init__(self):
        self.control = False
        self.id = 1
        self.lista_todos_numeros = []
        self.lista_ordenada = [1]
        self.status = ['Processing', 'Done', 'Inactive']

    async def download_link(self, url: str, session: ClientSession):
        async with session.get(url) as response:
            result = await response.json()
            #print(result)
            if result:

                numeros = result['numbers']
                #print(numeros)
                if not numeros:
                    #print("Final ", numeros)
                    self.control = True
                    return

                if 'numbers' not in result.keys():
                    print("Query error, ID ", id)
                    #print(result)


    async def download_all(self, id):
        my_conn = aiohttp.TCPConnector(limit=10)
        async with aiohttp.ClientSession(connector=my_conn) as session:
            tasks = []
            try:
                #print(self.id)
                #print("")
                valor_inicio = 1
                if id > 1:
                    valor_inicio = id/2
                for i in range(int(valor_inicio), id):
                    #print(i)
                    task = asyncio.ensure_future(self.download_link(url=str(f"http://challenge.dienekes.com.br/api/numbers?page={i}"), session=session))
                    tasks.append(task)
            except:
                pass


            await asyncio.gather(*tasks, return_exceptions=True)  # the await must be nest inside of the session

    def run(self):
        self.lista_ordenada.append(1)
        start = time.time()
        while not self.control:
            self.id = self.id * 2
            asyncio.run(self.download_all(self.id))
        end = time.time()
        print(f'Finalizado {end - start} segundos')
        self.ordenar()


    def ordenar(self):
        if len(self.lista_todos_numeros) == 1:
            listaOrdenada = []
            x = 0
            lista = self.lista_todos_numeros
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
            self.lista_ordenada = listaOrdenada


    def verificarStatus(self):
        print(self.lista_ordenada)
        if len(self.lista_ordenada) == 1:
            return self.status[2]
        elif len(self.lista_ordenada) == 2:
            return self.status[0]
        else:
            return self.status[1]


