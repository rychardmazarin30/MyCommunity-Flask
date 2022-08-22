# Formulários do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import login_user
from mycommunity.models import Usuario
import bcrypt

# Formulário de criar conta para um novo usuário
class FormCriarConta(FlaskForm):
    
    nome = StringField("Nome", validators=[DataRequired()])
    sobrenome = StringField("Sobrenome", validators=[DataRequired()])
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email("E-mail Inválido.")])
    password = PasswordField("Senha", validators=[DataRequired(), Length(8, 20, message="A sua senha tem que ter no mínimo 8 caracteres")])
    confirm_password = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo('password', message="O campo deve ser igual a senha.")])
    submit_button_registerAccount = SubmitField("Cadastrar-se")
    
    # Necessário função chamar validate_ pois só assim o FlaskForm(), consegue entender ela como um validator.
    # Essa função faz com que cada usuario seja único, não deixando ter e-mails e nem usernames repetidos.
    def validate_email(self, email):
        usuario_email = Usuario.query.filter_by(email=email.data).first()
        if usuario_email:
            raise ValidationError('E-mail já cadastrado.')
        else:
            pass
        
    def validate_username(self, username):
        usuario_username = Usuario.query.filter_by(username=username.data).first()
        if usuario_username:
            raise ValidationError('Nome de Usuário já cadastrado.')
        else:
            pass
        
# Formulário de fazer login em sua conta.
class FormLogin(FlaskForm):
    
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(8, 20)])
    submit_button_login = SubmitField("Login")
    
    def validate_email(self, email):
        global user
        user = Usuario.query.filter_by(email=email.data).first()
        if user:
            pass
        else:
            raise ValidationError("E-mail Não encontrado.")
    
    def validate_senha(self, senha):
        senha = senha.data
        senha = bytes(senha, 'utf-8')
        
        if user:
            if bcrypt.checkpw(senha, user.senha):
                login_user(user)
            else:
                raise ValidationError("Senha Incorreta")
        else:
            pass

