
import mysql.connector


mysql = mysql.connector
db_user ='root'
db_passwd = 'responsavel'
db_name = 'got'
db_host = '172.17.0.2'
def db_connect():
    return mysql.connect(user=db_user,password=db_passwd,host=db_host,database=db_name)
