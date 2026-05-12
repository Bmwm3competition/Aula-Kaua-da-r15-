from models.jogo_models import Jogo  
from db import db  
import json
from flask import make_response, request

def get_jogos():
    jogos = Jogo.query.all() 
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de jogos.',
            'dados': [jogo.json() for jogo in jogos]  
        }, ensure_ascii=False, sort_keys=False)  
    )
    response.headers['Content-Type'] = 'application/json' 
    return response


def get_jogo_by_id(jogo_id):
    Jogos = Jogo.query.get(jogo_id) 

    if jogo:  
        response = make_response(
            json.dumps({
                'mensagem': 'Jogo encontrado.',
                'dados': jogo.json()  
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
    
        response = make_response(
            json.dumps({'mensagem': 'Jogo não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  
        )
        response.headers['Content-Type'] = 'application/json'
        return response


    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in jogo_data for key in ['modelo', 'marca', 'ano']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Modelo, marca e ano são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    

    novo_jogo = jogo(
        fabricante=jogo_data['modelo'],
        marca=jogo_data['marca'],
        ano=jogo_data['ano']
    )
    
    db.session.add(novo_jogo) 
    db.session.commit()  

  
    response = make_response(
        json.dumps({
            'mensagem': 'Jogocadastrado com sucesso.',
            'jogo': novo_jogo.json() 
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  
    return response

def(jogo_id, jogo_data):
    jogo = Jogo.query.get(jogo_id) 

    if not jogo: 
        response = make_response(
            json.dumps({'mensagem': 'jogo não encontrado.'}, ensure_ascii=False),
            404 
        )
        response.headers['Content-Type'] = 'application/json'  

  
    if not all(key in jogo_data for key in ['modelo', 'marca', 'ano']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Modelo, marca e ano são obrigatórios.'}, ensure_ascii=False),
            400  
        )
        response.headers['Content-Type'] = 'application/json'  

   
    jogo.modelo = jogo_data['modelo']
    jogo.marca 'marca']
    jogo.ano = jogo_data['ano']

    db.session.commit() 

    
    response = make_response(
        json.dumps({
            'mensagem': 'jogo atualizado com sucesso.',
            'jogo': jogo.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  
    return response