from flask import Flask
from flask_restful import Api
from Numbers import DesafioAPI

app = Flask(__name__)
api = Api(app)


api.add_resource(DesafioAPI, '/numeros')

if __name__ == '__main__':
    app.run(debug=True)