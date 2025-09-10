from flask import Flask, jsonify, request 
app = Flask(__name__)

playlist = [
    {"id": 1, "titulo": "Sonne", "artista": "Rammestein"},
    {"id": 2, "titulo": "Monster", "artista": "skillet"},
    {"id": 3, "titulo": "Confess you love", "artista": "jiandro"},
    {"id": 4, "titulo": "Afro jazz", "artista": "frozy"},
]

@app.route('/musicas', methods=['GET'])
def get_musicas():
    return jsonify({"playlist": playlist, "total": len(playlist)})

@app.route("/musicas/<int:id>", methods=["GET"])
def get_musicas_by_id(id):
    for musica in playlist:
        if musica["id"] == id:
            return jsonify({"mensagem": "musica encontrada!", "musica": musica})
    
    return jsonify({"erro": "musica não encontrada!"}), 404

@app.route('/musicas',methods=['POST'])
def add_musicas():
    nova_musica = request.json

    nova_musica["id"] = len(playlist) + 1 

    playlist.append(nova_musica)
    return jsonify({"mensagem": "musica cadastrada com sucesso!","musica":nova_musica}), 201

@app.route("/musicas/<int:id>", methods=["PUT"])
def update_musica(id):
    dados = request.json

    for musica in playlist:
        if musica["id"] == id:
            musica.update(dados)
            return jsonify({"mensagem": " musica atualizada!", "musica": musica})
        
    return jsonify({"erro": "musica não encontrada!"}), 404

@app.route('/musicas/<int:id>', methods=["DELETE"])
def delete_musica(id):
    for musica in playlist:
        if musica["id"] == id:
            playlist.remove(musica)
            return jsonify({"musica": "musica deletada!"}), 200
    
    return jsonify({"erro": "musica não encontrada!"}), 404

if __name__ == '__main__':
    app.run(debug=True)