# 🔐 Password Manager API

API RESTful desenvolvida com **Flask** para gerenciamento de senhas (CRUD completo).
Permite criar, listar, atualizar e deletar senhas de forma simples.

---

## 🚀 Tecnologias utilizadas

* Python 3.x
* Flask
* JSON (para troca de dados)
* Postman (para testes)

---

## 📂 Estrutura do projeto

```
PASSWORD-MANAGER-FLASK/
│
├── models/
│   └── password.py
│
├── doc/
│   └── End-Points.postman_collection.json
│
├── venv/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/password-manager-flask.git
cd password-manager-flask
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

#### Windows:

```bash
venv\Scripts\activate
```

#### Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 📌 Endpoints da API

### 🔹 Criar senha

**POST** `/passwords`

#### Body (JSON)

```json
{
  "name": "gmail",
  "password": "123456"
}
```

#### Resposta

```json
{
  "message": "password successfully created and added to your passwords list"
}
```

---

### 🔹 Listar todas as senhas

**GET** `/passwords`

#### Resposta

```json
[
  {
    "id": 1,
    "name": "gmail",
    "password": "123456"
  }
]
```

---

### 🔹 Atualizar senha

**PUT** `/passwords/{id}`

#### Body (JSON)

```json
{
  "name": "gmail atualizado",
  "password": "nova_senha"
}
```

#### Resposta

```json
{
  "message": "password updated successfully!"
}
```

---

### 🔹 Deletar senha

**DELETE** `/passwords/{id}`

#### Resposta

```json
{
  "message": "password deleted successfully!"
}
```

---

## ⚠️ Validações implementadas

* Verificação se o JSON é válido
* Campos obrigatórios (`name` e `password`)
* Campos não podem ser vazios
* Retorno de erros com status HTTP adequados:

  * `400` → Requisição inválida
  * `404` → Recurso não encontrado

---

## 🧠 Conceitos aplicados

* API REST
* CRUD
* List Comprehension
* Programação Orientada a Objetos (POO)
* Manipulação de JSON
* Boas práticas com Flask

---

## 🧪 Testes com Postman

O projeto já inclui uma collection:

```
doc/End-Points.postman_collection.json
```

Basta importar no Postman para testar todos os endpoints.

Ou clicar no link abaixo:

    - link da collection no postman -> https://www.postman.com/lukasjean745-1800510/workspace/gerenciador-de-senhas

---

## 📌 Melhorias futuras

* 🔒 Criptografia de senhas
* 🗄️ Integração com banco de dados (SQLite/PostgreSQL)
* 🔐 Autenticação com JWT
* 📄 Documentação com Swagger/OpenAPI
* 🐳 Dockerização

---

## 👨‍💻 Autor

Desenvolvido por **Jean Lukas** 🚀
Projeto com foco em aprendizado de APIs REST com Flask.

---

## 📄 Licença

Este projeto está sob a licença MIT.

