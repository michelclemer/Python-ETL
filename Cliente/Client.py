import hashlib
#Aqui ficaria toda a logica para criar e gerenciar a chave do cliente

class Cliente:
    def __init__(self):
        #SHA1 = password
        self.chave = {'admin': '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'}

    def getKey(self):
        return self.chave

    def validarCliente(self, chave):
        for c, v in self.chave.items():
            if str(chave) == v:
                return True
        return False

    def adicionarCliente(self, chaveAdmin, nomeCliente, chaveCliente):
        if str(chaveAdmin) == self.chave['admin']:
            self.chave[nomeCliente] = hashlib.sha1(str(chaveCliente)).hexdigest()
            return "Cliente adicionado"
        return "Usuario admin inválido"



