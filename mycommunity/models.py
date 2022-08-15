# Tabelas do meu banco de dados
from mycommunity import database
from datetime import datetime

# Banco de dados dos Usuários
class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    sobrenome = database.Column(database.String, nullable=False)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)
    linguagens = database.Column(database.String, nullable=False, default='Não Informado')
    
    
# Banco de Dados dos posts dos usuários
class Post(database.Model):
    
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criação = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    
# Quando suas tabelas já estiverem criadas, vá até o console do python, importe de onde estiver esse arquivo
# E execute database.create_all(), suas tabelas serão criadas no banco de dados.