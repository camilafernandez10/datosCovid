# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
import mysql.connector
import csv
from mysql.connector import Error

def tomarConexión():
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
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        raise e
    


def cargarDatos():
    url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD'
    myfile = requests.get(url)
    open('datosCovid.csv', 'wb').write(myfile.content)
def leerDatos():
    with open('datosCovid.csv', newline='',encoding='cp850') as File:
        reader = csv.reader(File)
        conexion = tomarConexión()
        i =0
        for row in reader:
            if i==0:
                i=i+1
            else:
                sql="replace into datos (idCasos, fechaNotificacion, codigoDIVIPOLA, ciudad, departamento,atencion,edad,sexo,tipo,estado,paisProcedencia,fis,fechaDiagnostico, fechaRecuperado,fechaReporteWeb,tipoRec,codigoDepartamento,codigoPais,etnia) values (%s,'%s',%s,'%s','%s','%s',%s,'%s','%s','%s','%s','%s');"
                cursor1=conexion.cursor()
                cursor1.execute(sql) 
        conexion.commit()
        conexion.close()
cargarDatos()
leerDatos()


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
