import asyncio
import time
import aiohttp
from aiohttp.client import ClientSession


class ColetarDados:
    def __init__(self):
        self.control = False
        self.id = 1

    async def download_link(self, url: str, session: ClientSession):
        async with session.get(url) as response:
            result = await response.json()
            print(result)
            if result:

                numeros = result['numbers']
                print(numeros)
                if not numeros:
                    print("Final ", numeros)
                    self.control = True
                    return

                if 'numbers' not in result.keys():
                    print("Query error, ID ", id)
                    print(result)


    async def download_all(self, id):
        my_conn = aiohttp.TCPConnector(limit=10)
        async with aiohttp.ClientSession(connector=my_conn) as session:
            tasks = []
            try:
                print(self.id)
                print("")
                valor_inicio = 1
                if id > 1:
                    valor_inicio = id/2
                for i in range(int(valor_inicio), id):
                    print(i)
                    task = asyncio.ensure_future(self.download_link(url=str(f"http://challenge.dienekes.com.br/api/numbers?page={i}"), session=session))
                    tasks.append(task)
            except:
                pass


            await asyncio.gather(*tasks, return_exceptions=True)  # the await must be nest inside of the session

    def run(self):
        start = time.time()
        while not self.control:
            self.id = self.id * 2
            asyncio.run(self.download_all(self.id))
        end = time.time()
        print(f'Finalizado {end - start} segundos')


app = ColetarDados()
app.run()