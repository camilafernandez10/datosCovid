# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
import mysql.connector
import csv
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='DatosCovid',
                                         user='root',
                                         password='1234')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


def cargarDatos():
    url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD'
    myfile = requests.get(url)
    open('datosCovid.csv', 'wb').write(myfile.content)
def leerDatos():
    with open('datosCovid.csv', newline='') as File:
        reader = csv.reader(File)
        i=0
        for row in reader:
            print(row)
            if i<50:
                i=1+i
            else:
                break
cargarDatos()
leerDatos()


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
