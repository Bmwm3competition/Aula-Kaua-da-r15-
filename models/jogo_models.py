# Importa o objeto db de 'db', que fornece as funcionalidades do SQLAlchemy para interagir com o banco de dados
from db import db  

class Jogo(db.Model):  
    # Define o nome da tabela no banco de dados
    __tablename__ = 'jogo'  


    id = db.Column(db.Integer, primary_key=True)  
    modelo = db.Column(db.String(80), nullable=False)  
    marca = db.Column(db.String(80), nullable=False)  
    ano = db.Column(db.Integer, nullable=False)  
  
  
    def json(self):  
        return {
            'id': self.id,  
            'modelo': self.modelo, 
            'marca': self.marca, 
            'ano': self.ano }
