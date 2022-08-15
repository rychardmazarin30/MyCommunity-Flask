# Rotas do meu site
from flask import Flask, render_template, url_for, request, flash, redirect
from mycommunity import app, database
from mycommunity.forms import FormCriarConta, FormLogin
from mycommunity.models import Usuario, Post

users = Usuario.query.all()

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
        email = form_login.email.data
        senha = form_login.senha.data
        
        global usuario
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario:
            if senha == usuario.senha:
                flash("Login Efetuado com Sucesso!", 'alert-success')
                return redirect(url_for('welcome'))
            else:
                flash("Por favor, Verifique suas Informações e Tente Novamente.", 'alert-danger')
        else:
            flash("Por favor, Verifique suas Informações e Tente Novamente.", 'alert-danger')
                    
    return render_template("login.html", form_login=form_login)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form_createAccount = FormCriarConta()
    
    if form_createAccount.validate_on_submit() and 'submit_button_registerAccount' in request.form:
        
        # Cadastrando o usuário no banco de dados 
        usuario = Usuario(nome=form_createAccount.nome.data, sobrenome=form_createAccount.sobrenome.data, username=form_createAccount.username.data, email=form_createAccount.email.data, senha=form_createAccount.password.data)
        database.session.add(usuario)
        database.session.commit()
        
        flash("Cadastro Efetuado com Sucesso!", 'alert-success')
        return redirect(url_for('home'))
        
    return render_template("cadastro.html", form_createAccount=form_createAccount)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html", usuario=usuario)