from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from data import players
from game import handle_action
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")
CORS(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/players")
def get_players():
    return jsonify(players.values())

@app.route("/join", methods=["POST"])
def join():
    data = request.json
    players[data['id']] = data['name']
    return '', 204

@app.route("/action", methods=["POST"])
def action():
    data = request.json
    result = handle_action(data['id'], data['action'])
    return jsonify({"result": result})

# 接管前端路径，支持 React Router
@app.route("/<path:path>")
def serve_static_file(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
