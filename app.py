from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class DesafioAPI(Resource):

    def get(self):
        return {'numbers': 'n'}


api.add_resource(DesafioAPI, '/numeros')

if __name__ == '__main__':
    app.run(debug=True)