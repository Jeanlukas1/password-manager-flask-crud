from flask import Flask, request, jsonify
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
    Decisão única (um ou outro)	        elif """
    
    global id_control
    data = request.get_json()
    
    if not isinstance(data, dict):
        return jsonify({"error": "JSON must be an object"}), 400

    if "name" not in data or "password" not in data:
        return jsonify({"error": "Required fields remaining"}), 400

    if data["name"] == "" or data["password"] == "":
        return jsonify({"message": "Required fields remaining!"}), 400

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
        return jsonify({"message": "you dont have passwords created yet!"}), 404
    return jsonify([p.to_dict() for p in passwords]), 200

@app.route("/passwords/<int:id>", methods=["PUT"])
def update_passwords(id):
    """função que atualiza a senha com base no id fornecido no parametro da rota. Primeiro valido se há senhas na lista,
    se o Json é válido, se todos os campos estão preenchidos caso tudo isto for True, percorre-se a lista de objetos e
    verifica se o id inserido como parametro é igual algum id percorrido no loop, se sim, a senha é atualizada"""
    
    data = request.get_json()
    
    if not passwords:
        return jsonify({"message": "you dont have passwords created yet!"}), 404
    
    if not isinstance(data, dict):
        return jsonify({"error": "JSON must be an object"}), 400

    if "name" not in data or "password" not in data:
        return jsonify({"error": "Required fields remaining"}), 400

    if data["name"] == "" or data["password"] == "":
        return jsonify({"message": "Required fields remaining!"}), 400
    
    for p in passwords:
        if p.id == id:
            p.name = data["name"] 
            p.password = data["password"]
            return jsonify({"message": "password updated succefully!"}), 200
    return jsonify({"message": "id not found!"}), 404

@app.route("/passwords/<int:id>", methods=["DELETE"])
def delete_password(id):  
    """Função que deleta a senha cadastrada com base no id inserido no parametro da rota. Primeiro valido se a lista
    de passwords está vazia caso o contrario roda-se um loop e dentro do loop verifica-se se o id que foi passado
    no parametro bate com algum id dos objetos percorridos dentro do loop, se sim retorna um Json com a mensagem e
    status code 200."""
    
    if not passwords:
        return jsonify({"message": "you dont have passwords created yet!"}), 404
    
    for p in passwords:
        if p.id == id:
            passwords.remove(p)
            return jsonify({"message": "password deleted succefully!"}), 200
    return jsonify({"error": "id not found!"}), 404

if __name__ == "__main__":
    app.run(debug=True)