from flask import Blueprint, request  
from controllers.carro_controllers import get_carros, create_carro

# Define um Blueprint para as rotas de "Carro"
carro_routes = Blueprint('carro_routes', __name__)  

# Rota para listar todos os carros (GET)
@carro_routes.route('/Carro', methods=['GET'])
def carros_get():
    return get_carros()

# Rota para criar um novo carro (POST)
@carro_routes.route('/Carro', methods=['POST'])
def carros_post():
    return create_carro(request.json)

