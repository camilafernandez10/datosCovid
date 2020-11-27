from flask import Flask, jsonify, request
from flask_cors import CORS
from response import generarGraficas


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/destino', methods=['GET'])
def destino():
    response_object = {'status': 'success'}
    municipio = request.args.get('municipio','')
    departamento = request.args.get('departamento','')
    fecha = request.args.get('fecha','')
    data={
        'municipio': municipio,
        'departamento': departamento,
        'fecha': fecha
    }
    data2 = generarGraficas(data)
    response_object['data'] = data2
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()