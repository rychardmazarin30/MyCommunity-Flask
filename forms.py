from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormCriarConta(FlaskForm):
    
    username = StringField("Nome de Usuário", validators=[DataRequired(), ])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(8, 20)])
    confirm_password = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo('password')])
    submit_button_registerAccount = SubmitField("Cadastrar-se")
    

class FormLogin(FlaskForm):
    
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(8, 20)])
    lembrar_dados = BooleanField("Lembrar Dados")
    submit_button_login = SubmitField("Login")
    

