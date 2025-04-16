from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemplo de endpoint para simular armazenamento na nuvem
@app.route('/store-data', methods=['POST'])
def store_data():
    data = request.json
    # Lógica simulada para armazenamento (substituir por API de Cloud Storage real)
    response = {
        "message": "Dados armazenados com sucesso!",
        "data": data
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
