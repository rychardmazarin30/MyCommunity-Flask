from flask import Flask, render_template
app = Flask(__name__)

users = ["Rychard Mazarin", "Melissa Estephani", "Orlando Namba", "Gustavo Felix", "Sabrina Esther"]

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/contato")
def melhor():
    return render_template("contato.html")


@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", users=users)


if __name__ == "main":
    app.run(debug=True)
    