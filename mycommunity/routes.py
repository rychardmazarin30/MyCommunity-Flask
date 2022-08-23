# Rotas do meu site
from flask import Flask, render_template, url_for, request, flash, redirect
from mycommunity import app, database
from mycommunity.forms import FormCriarConta, FormEditPassword, FormLogin, FormEditProfile, FormEditPassword
from mycommunity.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required
import bcrypt


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/membros")
@login_required
def membros():
    users = Usuario.query.all()
    return render_template("members.html", users=users)


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = FormLogin()
    
    if form_login.validate_on_submit() and 'submit_button_login' in request.form:
        global usuario
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        login_user(usuario)
        flash("Login Efetuado com Sucesso!", 'alert-success')
        next_parameter = request.args.get('next')
        if next_parameter:
            return redirect(next_parameter)
        else:
            return redirect(url_for('home'))

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
        
        login_user(usuario)
        flash("Cadastro Efetuado com Sucesso!", 'alert-success')
        return redirect(url_for('home'))
        
    return render_template("cadastro.html", form_createAccount=form_createAccount)


@app.route("/profile")
@login_required
def profile():
    profile_photo = url_for('static', filename='profile_photos/{}'.format(current_user.foto_perfil))
    return render_template("profile.html", profile_photo=profile_photo)


@app.route('/profile/edit', methods=["GET", "POST"])
@login_required
def edit_profile():
    form_edit = FormEditProfile()
    
    profile_photo = url_for('static', filename='profile_photos/{}'.format(current_user.foto_perfil))
    return render_template('profile_edit.html', profile_photo=profile_photo, form_edit=form_edit)


@app.route('/profile/edit/password', methods=["GET", "POST"])
@login_required
def edit_password():
    form_edit_password = FormEditPassword()
    
    profile_photo = url_for('static', filename='profile_photos/{}'.format(current_user.foto_perfil))
    return render_template('profile_edit_password.html', profile_photo=profile_photo, form_edit_password=form_edit_password)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout Efetuado com Sucesso.', 'alert-success')
    return redirect(url_for('home'))


@app.route('/post/create')
@login_required
def create_post():
    return render_template('create_post.html')
