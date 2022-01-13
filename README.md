# Python-ETL
Aplicação que realize um processo de ETL (Extract, Transform and Load)

# Visão Geral

Aplicaçõe feita em Python3.8 utilizando o framework Flask para coletar dados de uma API e disponibilizar em uma API REST.

## Instalação

Utilizar o ``` pip ``` Para instalar as dependencias:

```
pip install -r requirements.txt

```

Iniciar API:

```
@root:~$ Python app.py
```

## Iniciar API 


**A API está rodando no endereço http://127.0.0.1:5000/numeros**

O sistema de coleta de dados será iniciado quando enviar um ``` POST ``` para o endereço ``` /numeros ``` :

URL: 

```
http://127.0.0.1:5000/numeros

```

JSON:

```
{
    "clientKey": "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8",
    "type": "init"       
}
```
A chave **clientKey** representa a credencial de usuário válida para enviar comandos para API. Nesse caso, é a hash SHA1 da palavra **password**.



## Visualizar dados

Após realizar o POST, os dados ficaram disponiveis ao realizar um GET para ``` /numeros ``` .

O resultado da solicitação será:
```
{
    "status": "Processing",
    "numbers": [
        1,
        1
    ]
}
```

Todos os dados podem demorar alguns minutos para serem carregados na API. Mas os resultados devem ser ordenados e seram imprimidos no intervalo de alguns segundos.

### Informações adicionais

Respostas:

Chave ``` status ``` :

**Processing** : Processando a requisição.

**Done** : Processo finalizado.

**Inactive** : Aguardando instruções.


Chave ``` type ``` :

**init** : Instrução para iniciar a coleta dos dados.

