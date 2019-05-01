from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import  query_sql
import time, json

#
app = Flask(__name__)
mysqlflask = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'GOT'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysqlflask.init_app(app)

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

@app.route('/book/', methods=['POST', 'DELETE', 'PUT'])
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
                return "Error Method not allowed!!"

@app.route('/house/', methods=['POST', 'DELETE', 'PUT'])
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
                return "Error Method not allowed!!"

@app.route('/character/', methods=['POST', 'DELETE','PUT'])
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
                return "Error Method not allowed!"

# Classes Get
def get_value(information):
    db_connect()
    a = mysqlflask.connect().cursor()
    a.execute('''select * from ''' + db_name + '''.houses where name = "''' + information + '''";''')
    b = mysqlflask.connect().cursor()
    b.execute('''select * from ''' + db_name + '''.characters where name = "''' + information + '''";''')
    c = mysqlflask.connect().cursor()
    c.execute('''select * from ''' + db_name + '''.books where name = "''' + information + '''";''')        
    r = [dict((a.description[i][0], value)
            for i, value in enumerate(row)) for row in a.fetchall()]
    s = [dict((b.description[i][0], value)
            for i, value in enumerate(row)) for row in b.fetchall()]
    t = [dict((c.description[i][0], value)
            for i, value in enumerate(row)) for row in c.fetchall()]
    print (t)

    return jsonify({'Valores em Json' : r + s + t})

def get_values():
    db_connect()
    a = mysqlflask.connect().cursor()
    a.execute('''select * from ''' + db_name + '''.houses order by name;''')
    b = mysqlflask.connect().cursor()
    b.execute('''select * from ''' + db_name + '''.characters order by name;''')
    c = mysqlflask.connect().cursor()
    c.execute('''select * from ''' + db_name + '''.books order by name;''')
        
    r = [dict((a.description[i][0], value)
            for i, value in enumerate(row)) for row in a.fetchall()]
    s = [dict((b.description[i][0], value)
            for i, value in enumerate(row)) for row in b.fetchall()]
    t = [dict((c.description[i][0], value)
            for i, value in enumerate(row)) for row in c.fetchall()]

    return jsonify({'Valores em Json' : r + s + t})

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

# Run 
if __name__ == '__main__':
    app.run()