
import mysql.connector


mysql = mysql.connector
db_user ='root'
db_passwd= ''
db_name = 'GOT'
db_host='localhost'
def db_connect():
    return mysql.connect(user=db_user,password=db_passwd,host=db_host,database=db_name)