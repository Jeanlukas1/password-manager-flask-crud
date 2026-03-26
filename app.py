from flask import Flask, url_for, request, jsonify
from models.password import Password

app = Flask(__name__)

passwords = []
id_control = 1


@app.route("/passwords", methods=["POST"])
def create_password():
    """if isolado pois estamos fazendo uma validação isolada da outra, caso o contrário o elif seria mais apropriado
    por exemplo caso eu quisesse que uma das validações abaixo fosse true, porém eu quero que todas sejam checadas
        Situação	                    Use
    Validações independentes	      if separados 
    Decisão única (um ou outro)	  elif """
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
    """List-comprehention Expressão/oque eu quero que esta variavel temporaria faça ou gere, no caso a variavel temporaria
    percorrera cada objeto e formatará cada objeto dentro de passowords. o to_dict() é como se fosse uma variável de 
    apresentação porém em formato dicionario pois precisamos converter este objeto em um dicionário depois para Json
    pois não podemos utilizar objetos para trafegar dados"""
    if not passwords:
        return jsonify({"Message": "Lista Vazia, adicione uma tarefa na sua lista"}), 404
    return jsonify([p.to_dict() for p in passwords]), 200

if __name__ == "__main__":
    app.run(debug=True)