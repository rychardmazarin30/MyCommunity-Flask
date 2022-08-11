# Arquivo main
from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCriarConta, FormLogin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

users = ["Rychard Mazarin", "Melissa Estephani", "Orlando Namba", "Gustavo Felix", "Sabrina Esther"]

app.config["SECRET_KEY"] = '50ef59056578f21b0daf78ca4d7b823e'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///community.db'

database = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", users=users)

@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = FormLogin()
    
    if form_login.validate_on_submit() and 'submit_button_login' in request.form:
        flash("Login Efetuado com Sucesso!", 'alert-success')
        return redirect(url_for('home'))
    
    return render_template("login.html", form_login=form_login)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form_createAccount = FormCriarConta()
    
    if form_createAccount.validate_on_submit() and 'submit_button_registerAccount' in request.form:
        flash("Cadastro Efetuado com Sucesso!", 'alert-success')
        return redirect(url_for('home'))
        
    return render_template("cadastro.html", form_createAccount=form_createAccount)

if __name__ == "main":
    app.run(debug=True)
    