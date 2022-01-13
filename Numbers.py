from flask_restful import Resource,reqparse
from Cliente.Client import Cliente
from Resource.GetData import ColetarDados
import threading


Cliente = Cliente()
numeros_dados = ColetarDados()


class DesafioAPI(Resource):
    def get(self):
        return {'status':numeros_dados.verificarStatus(), 'numbers': numeros_dados.lista_ordenada}

    def post(self):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('clientKey')
        argumentos.add_argument('type')

        dados = argumentos.parse_args()

        cliente_valido = Cliente.validarCliente(dados['clientKey'])
        if cliente_valido and dados['type'] == 'init':
            t = threading.Thread(target=numeros_dados.run)
            t.start()
            return {'status':numeros_dados.verificarStatus(), 'numbers': numeros_dados.lista_ordenada}
        else:
            return {"Message": 'Error, invalid key or type'}

