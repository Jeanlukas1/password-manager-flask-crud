from flask import Flask, url_for

app = Flask(__name__)

@app.route("/site/<username>")
def user(username):
    url_for("/user", username = username)
    
    
if __name__ == "__main__":
    app.run(debug=True)