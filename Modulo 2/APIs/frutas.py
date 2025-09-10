from flask import Flask, jsonify, request
app = Flask(__name__)

frutas = [
    {"id": 1, "nome": "maca", "cor": "vemelha"},
    {"id": 2, "nome": "banana", "cor": "amarela"},
]

@app.route('/frutas', methods=['GET'])
def get_frutas():
    return jsonify({"frutas": frutas, "total": len(frutas)})

@app.route('/frutas', methods=['POST'])
def add_fruta():
    nova_fruta = request.json

    nova_fruta["id"] = len(frutas) + 1

    frutas.append(nova_fruta)
    return jsonify({"mensagem": "fruta adicionada!", "fruta": nova_fruta}), 201

@app.route('/frutas/<int:id>',methods=['PUT'])
def update_fruta(id):
    dados = request.json

    for fruta in frutas:
        if fruta["id"] == id:
            fruta.update(dados)
            return jsonify({"mesagem": "fruta atualizada!", "fruta": fruta})
    return jsonify({"erro": "frutas  não encontrada!"}), 404

@app.route('/frutas/<int:id>', methods=["DELETE"])
def delete_fruta(id):
    for fruta in frutas:
        if fruta["id"] == id:
            frutas.remove(frutas)
            return jsonify({"fruta": "fruta removida!"}), 200

    return jsonify({"erro": "fruta não encontada!"}), 404

if __name__ == '__main__':
    app.run(debug=True)