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
    print("Descargando archivo de datos")
    open('datosCovid.csv', 'wb').write(myfile.content)
    print("Archivo descargado satisfactoriamente")
def leerDatos():
    print("Inicio de carga de datos")
    with open('datosCovid.csv', newline='',encoding='cp850') as File:
        reader = csv.reader(File)
        conexion = tomarConexión()
        contador=0
        i=0
        cursor1=conexion.cursor()
        for row in reader:
            if i==0:
                i=i+1
            else:
                sql="replace into datos (idCasos, fechaNotificacion, codigoDIVIPOLA, ciudad, departamento,atencion,edad,sexo,tipo,estado,paisProcedencia,fis,fechaDeMuerte,fechaDiagnostico, fechaRecuperado,fechaReporteWeb,tipoRec,codigoDepartamento,codigoPais,etnia,nombreGrupoEtnico) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                for it in range(len(row)):
                    if str(row[it])=="":
                        row[it]=None
                cursor1.execute(sql,(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20])) 
                print("Cargando base de datos: "+str(contador) )# int((i/reader.line_num))*100)
                contador=contador+1
        conexion.commit()
        conexion.close()

cargarDatos()
leerDatos()


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
