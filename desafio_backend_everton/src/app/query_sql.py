
try:
        import json as simplejson
except ImportError:
        import simplejson
from  connect_mysl import db_connect as mysql
import time
from flask import jsonify
from urllib2 import quote

def time_now():
    datetime = time.strftime(r"%Y-%m-%d ",time.localtime())
    return datetime

# Define a function/callable to be called on every string_json
def insert_book(string_json):
        twitdb = mysql()
        set_json = string_json
        for i, item in enumerate(set_json):
                id = item.get('id')
                name = tostr(item.get('name'))
                pages = item.get('pages')
                preceded_by = item.get('preceded_by')
                followed_by = item.get('followed_by')
                release_date = tostr(item.get('release_date'))
                twitdb.cursor().execute ("INSERT INTO books (id, name, pages, preceded_by, followed_by, release_date) values(%s,%s,%s,%s,%s,%s);",(id, name, pages, preceded_by, followed_by, release_date))
        twitdb.commit()
        twitdb.close()

def insert_house(string_json):
        twitdb = mysql()
        set_json = string_json
        for i, item in enumerate(set_json):
                id = item.get('id')
                name = item.get('name')
                places =tostr(item.get('places'))
                region = tostr(item.get('region'))
                coat_of_arms = tostr(item.get('coat_of_arms'))
                words = item.get('words')
                founder = item.get('founder')
                current_lord = item.get('current_lord')
                heir =item.get('heir')
                ancestral_weapons = tostr(item.get('ancestral_weapons'))
                twitdb.cursor().execute ("INSERT INTO houses (id, name, places, region, coat_of_arms, words, founder, current_lord, heir, ancestral_weapons) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (id, name, places, region, coat_of_arms, words, founder, current_lord, heir, ancestral_weapons))
        twitdb.commit()
        twitdb.close()
    
def insert_character(string_json):
        twitdb = mysql()
        set_json = string_json
        for i, item in enumerate(set_json):
                id = item.get('id')
                name = item.get('name')
                gender =tostr(item.get('gender'))
                culture = tostr(item.get('culture'))
                titles = tostr(item.get('titles'))
                aliases = tostr(item.get('aliases'))
                born = tostr(item.get('born'))
                died = tostr(item.get('died'))
                father =item.get('father')
                mother = item.get('mother')
                spouse = item.get('spouse')
                children = toint(item.get('children'))
                books = toint(item.get('books'))
                twitdb.cursor().execute ("INSERT INTO characters (id, name, gender, culture, titles, aliases, born,\
                                                                 died, father, mother, spouse, children, books) \
                                                                 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", 
                                                                 (id, name, gender, culture, titles, aliases, born, died,
                                                                 father, mother, spouse, children, books))
        twitdb.commit()
        twitdb.close()

def update_book(string_json):
        twitdb = mysql()
        set_json = string_json
        for i, item in enumerate(set_json):
                id = item.get('id')
                name = tostr(item.get('name'))
                pages = item.get('pages')
                preceded_by = item.get('preceded_by')
                followed_by = item.get('followed_by')
                release_date = tostr(item.get('release_date'))
                twitdb.cursor().execute ("UPDATE books set name = %s, pages = %s, preceded_by = %s, followed_by = %s , release_date = %s \
                                         WHERE id = %s ;",( name, pages, preceded_by, followed_by, release_date, id))
        twitdb.commit()
        twitdb.close()

def update_house(string_json):
        twitdb = mysql()
        set_json = string_json
        for i, item in enumerate(set_json):
                id = item.get('id')
                name = item.get('name')
                places =tostr(item.get('places'))
                region = tostr(item.get('region'))
                coat_of_arms = tostr(item.get('coat_of_arms'))
                words = item.get('words')
                founder = item.get('founder')
                current_lord = item.get('current_lord')
                heir =item.get('heir')
                ancestral_weapons = tostr(item.get('ancestral_weapons'))
                twitdb.cursor().execute ("UPDATE houses set name = %s, places = %s, region = %s, coat_of_arms = %s, words = %s, \
                                          founder = %s, current_lord = %s, heir = %s, ancestral_weapons = %s       \
                                          WHERE id = %s ;",( name, places, region, coat_of_arms, words, founder, current_lord,
                                          heir, ancestral_weapons, id))
        twitdb.commit()
        twitdb.close()

def update_character(string_json):
        twitdb = mysql()
        set_json = string_json
        for i, item in enumerate(set_json):
                id = item.get('id')
                name = item.get('name')
                gender =tostr(item.get('gender'))
                culture = tostr(item.get('culture'))
                titles = tostr(item.get('titles'))
                aliases = tostr(item.get('aliases'))
                born = tostr(item.get('born'))
                died = tostr(item.get('died'))
                father =item.get('father')
                mother = item.get('mother')
                spouse = item.get('spouse')
                children = toint(item.get('children'))
                books = toint(item.get('books'))
                twitdb.cursor().execute ("UPDATE characters set name = %s, gender = %s, culture = %s, titles = %s, aliases = %s, \
                                          born = %s, died = %s, father = %s, mother = %s, spouse = %s, children = %s, books =%s \
                                          WHERE id = %s ;",( name, gender, culture, titles, aliases, born, died, father, mother,
                                          spouse, children, books, id))

        twitdb.commit()
        twitdb.close()

def remove_book(string_json):
        twitdb = mysql()
        set_json = string_json
        for i, item in enumerate(set_json):
                id = str(item.get('id'))
                twitdb.cursor().execute ("DELETE FROM books where id = "+id+" ;")
        twitdb.commit()
        twitdb.close()

def remove_house(string_json):
        twitdb = mysql()
        set_json = string_json
        for i, item in enumerate(set_json):
                id = str(item.get('id'))
                twitdb.cursor().execute ("DELETE FROM houses where id = "+id+" ;")
        twitdb.commit()
        twitdb.close()

def remove_character(string_json):

        twitdb = mysql()
        set_json = string_json
        for i, item in enumerate(set_json):
                id = str(item.get('id'))
                twitdb.cursor().execute ("DELETE FROM characters where id = "+id+" ;")
        twitdb.commit()
        twitdb.close()

def tostr(list):
        if list == None:
                return list
        
        s = [str(i.encode('utf-8')) for i in list]
        listed = str("".join(s))

        return listed

def toint(list):
        
        if list == None:
                return list
        
        s = [str(i) for i in list]
        listed = str(",".join(s))

        return listed


