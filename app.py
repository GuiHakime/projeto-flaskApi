from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource
import sqlalchemy
import os
from datetime import datetime

basedir = os.path.dirname(os.path.realpath(__file__))

print(basedir)
app = Flask(__name__)

api = Api(app)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'books.db')  # Usando SQLite, substitua conforme necessário
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa o rastreamento de modificações para evitar um aviso
app.config['SQLALCHEMY_ECHO'] = True #Config para criar a primeira tabela


#Criar instância do db
db = SQLAlchemy(app)

class Book_res(db.Model):
    id=db.Column(db.Integer(), primary_key=True) #Primary_key sempre é o ID
    title = db.Column(db.String(80), nullable = False)
    autor = db.Column(db.String(40), nullable = False)
    date_added = db.Column(db.DateTime(), default = datetime.utcnow)

#Sempre preciso de um retorno então escolho o título
    def __repr__(self):
        return self.title

@api.route('/books')   #ROTA apenas para postar
class Books(Resource):
    def get(self):
        return jsonify({"message": "HelloWorld"})
    
    def post(self):
        pass
                             #ROTA para interagir através do ID
@api.route('/books<int:id>')  #Colocar um ID para rotaurl, para toda vez achar em qual função ira
class BookResource(Resource):
    def get(self, id):
        pass
    
    def put(self, id):
        pass
    
    def delete(self, id):
        pass
    

@app.shell_context_processor
def make_shell_context():
    return{
        'db':db,
        'Book_res':Book_res
    }
    
    
if __name__ == "__main__":
    app.run(debug=True)