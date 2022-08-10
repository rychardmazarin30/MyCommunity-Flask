from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)

users = ["Rychard Mazarin", "Melissa Estephani", "Orlando Namba", "Gustavo Felix", "Sabrina Esther"]

app.config["SECRET_KEY"] = '50ef59056578f21b0daf78ca4d7b823e'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", users=users)

@app.route("/login")
def login():
    form_login = FormLogin()
    return render_template("login.html",form_login=form_login)

@app.route("/cadastro")
def cadastro():
    form_createAccount = FormCriarConta()
    return render_template("cadastro.html", form_createAccount=form_createAccount)

if __name__ == "main":
    app.run(debug=True)
    