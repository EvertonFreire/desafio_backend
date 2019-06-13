import json

from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

from .query_sql import *

#
app = Flask(__name__)
mysqlflask = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'responsavel'
app.config['MYSQL_DATABASE_DB'] = 'got'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysqlflask.init_app(app)

use_docker = False


# Classes App Route
@app.route('/search/id/<path:information>', methods=['GET'])
def search_id(information):
    if request.method == 'GET':
        if information != None:
            return get_value(information)
        else:
            return "Error value is null."
    else:
        return "Error Method not allowed!!"

@app.route('/search/', methods=['GET'])
def search():
    if request.method == 'GET':
        return get_values()
    else:
        return "Error Method not allowed!!"

@app.route('/book/', methods=['POST', 'DELETE', 'PUT','GET'])
def book():
    if request.method == 'POST':
        book_json = request.data
        book = json.loads(book_json)
        return post_book(book)
    else: 
        if request.method == 'DELETE':
            book_json = request.data
            book = json.loads(book_json)
            return delete_book(book)
        else:
            if request.method == 'PUT':
                book_json = request.data
                book = json.loads(book_json)
                return update_book(book)
            else: 
                if request.method == 'GET':
                    return list_book()
                else:
                    return "Error Method not allowed!!"

@app.route('/house/', methods=['POST', 'DELETE', 'PUT', 'GET'])
def house():
    if request.method == 'POST':
        house_json = request.data
        house = json.loads(house_json)
        return post_house(house)
    else: 
        if request.method == 'DELETE':
            house_json = request.data
            house = json.loads(house_json)
            return delete_house(house)
        else:
            if request.method == 'PUT':
                house_json = request.data
                house = json.loads(house_json)
                return update_house(house)
            else: 
                if request.method == 'GET':
                    return list_house()
                else:
                    return "Error Method not allowed!!"

@app.route('/character/', methods=['POST', 'DELETE','PUT', 'GET'])
def character():
    if request.method == 'POST':
        character_json = request.data
        character = json.loads(character_json)
        return post_character(character)
    else: 
        if request.method == 'DELETE':
            character_json = request.data
            character = json.loads(character_json)
            return delete_character(character)
        else:
            if request.method == 'PUT':
                character_json = request.data
                character = json.loads(character_json)
                return update_character(character)
            else: 
                if request.method == 'GET':
                    return list_character()
                else:
                    return "Error Method not allowed!!"

# Classes Get
def get_value(information):

    a = mysqlflask.connect().cursor()
    a.execute('''select * from ''' + app.config['MYSQL_DATABASE_DB'] + '''.houses where name = "''' + information + '''";''')
    b = mysqlflask.connect().cursor()
    b.execute('''select * from ''' + app.config['MYSQL_DATABASE_DB'] + '''.characters where name = "''' + information + '''";''')
    c = mysqlflask.connect().cursor()
    c.execute('''select * from ''' + app.config['MYSQL_DATABASE_DB'] + '''.books where name = "''' + information + '''";''')        
    r = [dict((a.description[i][0], value)
            for i, value in enumerate(row)) for row in a.fetchall()]
    s = [dict((b.description[i][0], value)
            for i, value in enumerate(row)) for row in b.fetchall()]
    t = [dict((c.description[i][0], value)
            for i, value in enumerate(row)) for row in c.fetchall()]

    return jsonify({'Valores em Json' : r + s + t})

def get_values():
    
    a = mysqlflask.connect().cursor()
    a.execute('''select * from ''' + app.config['MYSQL_DATABASE_DB'] + '''.houses;''')
    b = mysqlflask.connect().cursor()
    b.execute('''select * from ''' + app.config['MYSQL_DATABASE_DB'] + '''.characters;''')
    c = mysqlflask.connect().cursor()
    c.execute('''select * from ''' + app.config['MYSQL_DATABASE_DB'] + '''.books;''')        
    r = [dict((a.description[i][0], value)
            for i, value in enumerate(row)) for row in a.fetchall()]
    s = [dict((b.description[i][0], value)
            for i, value in enumerate(row)) for row in b.fetchall()]
    t = [dict((c.description[i][0], value)
            for i, value in enumerate(row)) for row in c.fetchall()]

    return jsonify({'Valores em Json:' : r +s +t})

def list_book():
    
    book = mysqlflask.connect().cursor()
    book.execute('''select * from ''' + app.config['MYSQL_DATABASE_DB'] + '''.books;''')        
    
    book_result = [dict((book.description[i][0], value)
            for i, value in enumerate(row)) for row in book.fetchall()]

    return jsonify({'Valores em Json:' : book_result})

def list_house():
    
    house = mysqlflask.connect().cursor()
    house.execute('''select * from ''' + app.config['MYSQL_DATABASE_DB'] + '''.houses;''')        
    
    house_result = [dict((house.description[i][0], value)
            for i, value in enumerate(row)) for row in house.fetchall()]

    return jsonify({'Valores em Json:' : house_result})

def list_character():
    
    character = mysqlflask.connect().cursor()
    character.execute('''select * from ''' + app.config['MYSQL_DATABASE_DB'] + '''.characters;''')        
    
    character_result = [dict((character.description[i][0], value)
            for i, value in enumerate(row)) for row in character.fetchall()]

    return jsonify({'Valores em Json:' : character_result})

# Classes Post
def post_book(book):
    query_sql.insert_book(book)
    return '''Livro cadastrado.'''

def post_house(house):
    query_sql.insert_house(house)
    return '''Casa cadastrada.'''

def post_character(character):
    query_sql.insert_character(character)
    return '''Personagem Cadastrado.'''

# Classes Update
def update_book(book):
    query_sql.update_book(book)
    return "O livro foi alterado."

def update_house(house):
    query_sql.update_house(house)
    return "As informacoes da Casa foram alteradas."

def update_character(character):
    query_sql.update_character(character)
    return "As informacoes do personagem foram alteradas."
    

# Classes Delete
def delete_book(book):
    query_sql.remove_book(book)
    return '''Livro removido.'''

def delete_house(house):
    query_sql.remove_house(house)
    return '''Casa removida.'''

def delete_character(character):
    query_sql.remove_character(character)
    return '''Personagem removido.'''


def create_db():
    use_docker = True
    if use_docker == True:
        import os
        file = open('/usr/local/projeto/desafio_backend/desafio_backend_everton/src/app/docker.sh')
        bash = "".join(file.readlines())
        os.system(bash)
        file = open('/usr/local/projeto/desafio_backend/desafio_backend_everton/src/app/db_config.sql')
        sql = "".join(file.readlines())
        from desafio_backend_everton.src.app import connect_mysl
        connect_mysl.db_connect()
        query_sql.mysql()
        cursor = query_sql.mysql()
        cursor.cursor().execute(sql, multi=True)
        query_sql.mysql().cmd_query_iter(query_sql.mysql().commit())
    else:
        file = open('/usr/local/projeto/desafio_backend/desafio_backend_everton/src/app/db_config.sql')
        sql = "".join(file.readlines())
        query_sql.mysql()
        cursor = query_sql.mysql().cursor()
        cursor.execute(sql, multi=True)
        query_sql.mysql().cmd_query_iter(query_sql.mysql().commit())

# Run 
if __name__ == '__main__':
    try:
        create_db()
    except Exception as e:
        print(e)
    app.run()
