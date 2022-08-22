# Rotas do meu site
from flask import Flask, render_template, url_for, request, flash, redirect
from mycommunity import app, database
from mycommunity.forms import FormCriarConta, FormLogin
from mycommunity.models import Usuario, Post
import bcrypt
from flask_login import login_user

users = Usuario.query.all()


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", users=users)


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = FormLogin()
    
    if form_login.validate_on_submit() and 'submit_button_login' in request.form:
        global usuario
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        flash("Login Efetuado com Sucesso!", 'alert-success')
        return redirect(url_for('welcome'))

    return render_template("login.html", form_login=form_login)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form_createAccount = FormCriarConta()
    
    if form_createAccount.validate_on_submit() and 'submit_button_registerAccount' in request.form:
        
        # Criptografando senha usuário
        pw = form_createAccount.password.data
        pw = bytes(pw, 'utf-8')
        salt = bcrypt.gensalt(8)
        
        senha_cript = bcrypt.hashpw(pw, salt)
        # Cadastrando o usuário no banco de dados 
        usuario = Usuario(nome=form_createAccount.nome.data.capitalize(), sobrenome=form_createAccount.sobrenome.data.capitalize(), username=form_createAccount.username.data, email=form_createAccount.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        
        flash("Cadastro Efetuado com Sucesso!", 'alert-success')
        return redirect(url_for('home'))
        
    return render_template("cadastro.html", form_createAccount=form_createAccount)


@app.route("/welcome")
def welcome():
    return render_template("welcome.html", usuario=usuario)