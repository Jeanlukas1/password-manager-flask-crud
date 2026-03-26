from flask import Flask, url_for, request, jsonify
from models.password import Password

app = Flask(__name__)

passwords = []
id_control = 1


@app.route("/passwords", methods=["POST"])
def create_password():
    global id_control
    data = request.get_json()

    if not isinstance(data, dict):
        return jsonify({"error": "JSON deve ser um objeto"}), 400

    if "name" not in data or "password" not in data:
        return jsonify({"error": "Campos obrigatórios faltando"}), 400

    if data["name"] == "" or data["password"] == "":
        return jsonify({"message": "Campos obrigatórios não preenchidos!"}), 400

    new_password = Password(
        id=id_control,
        name=data["name"],
        password=data["password"]
    )
    id_control += 1
    passwords.append(new_password)
    return jsonify({"message": "password succefully created and added to your passwords list"}), 200

@app.route("/passwords", methods=["GET"])
def list_passwords():
    

if __name__ == "__main__":
    app.run(debug=True)