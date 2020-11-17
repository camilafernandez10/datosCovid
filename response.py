#!C:/Users/Lenovo/Anaconda3/python.exe
#aquí va el intérprete

import mysql.connector
from mysql.connector import errorcode
import json
import cgi
import os

print('Content-Type: text/json')
print('')


datos= cgi.FieldStorage()
if os.environ['REQUEST_METHOD']=="POST":
    print("post")
elif os.environ['REQUEST_METHOD']=="PUT":
    print("put")
elif os.environ['REQUEST_METHOD']=="DELETE":
    print("delete")
elif os.environ['REQUEST_METHOD']=="GET":
    departamento=datos.getvalue('departamento')
    sql = "select d"