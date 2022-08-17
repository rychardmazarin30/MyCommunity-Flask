# Formulários do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from mycommunity.models import Usuario

# Formulário de criar conta para um novo usuário
class FormCriarConta(FlaskForm):
    
    nome = StringField("Nome", validators=[DataRequired()])
    sobrenome = StringField("Sobrenome", validators=[DataRequired()])
    username = StringField("Nome de Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(8, 20)])
    confirm_password = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo('password')])
    submit_button_registerAccount = SubmitField("Cadastrar-se")
    
    # Necessário função chamar validate_ pois só assim o FlaskForm(), consegue entender ela como um validator.
    # Essa função faz com que cada usuario seja único, não deixando ter e-mails e nem usernames repetidos.
    def validate_email(self, email):
        usuario_email = Usuario.query.filter_by(email=email.data).first()
        if usuario_email:
            raise ValidationError('E-mail already registered.')
        else:
            pass
        
    def validate_username(self, username):
        usuario_username = Usuario.query.filter_by(username=username.data).first()
        if usuario_username:
            raise ValidationError('Username already exists.')
        else:
            pass
        
# Formulário de fazer login em sua conta.
class FormLogin(FlaskForm):
    
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    submit_button_login = SubmitField("Login")
    

