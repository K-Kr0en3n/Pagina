from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hola desde Python 🐍</h1>
    <p>Tu servidor funciona correctamente</p>
    """

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"<h2>Hola, {nombre} 👋</h2>"

if __name__ == "__main__":
    app.run(debug=True)
