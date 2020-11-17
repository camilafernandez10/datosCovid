# This is a sample Python script.

# Descargar los datos y Actualizar los datos

import requests
import mysql.connector
import csv
from mysql.connector import Error
import datetime

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
    


def cargarDatosPais():
    url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD'
    myfile = requests.get(url)
    print("Descargando archivo de datos (Colombia)")
    open('datosCovid.csv', 'wb').write(myfile.content)
    print("Archivo descargado satisfactoriamente")
def leerDatosPais():
    print("Inicio de carga de datos")
    with open('datosCovid.csv', newline='',encoding='utf-8') as File:
        reader = csv.reader(File)
        conexion = tomarConexión()
        contador=0
        cursor1=conexion.cursor()
        for row in reader:
            if contador==0:
                contador=1
            else:
                sql="replace into datos (fecha_reporte_web,idCaso, fecha_de_notificacion, departamento,municipio,edad,sexo,tipoContagio,ubicacion,estado,paisProcedencia,recuperado,fecha_inicio_sintomas,fecha_de_muerte,fecha_diagnostico,fecha_de_recuperacion,tipo_recuperacion,nombreGrupoEtnico) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                for it in range(len(row)):
                    if str(row[it])=="":
                        row[it]=None
                if row[0]is not None:
                    row[0]=datetime.datetime.strptime(row[0], '%d/%m/%Y %H:%M:%S')
                if row[2]is not None:
                    row[2]=datetime.datetime.strptime(row[2], '%d/%m/%Y %H:%M:%S')
                if row[16]is not None:
                    row[16]=datetime.datetime.strptime(row[16], '%d/%m/%Y %H:%M:%S')
                if row[17]is not None:
                    row[17]=datetime.datetime.strptime(row[17], '%d/%m/%Y %H:%M:%S')
                if row[18]is not None:
                    row[18]=datetime.datetime.strptime(row[18], '%d/%m/%Y %H:%M:%S')
                if row[19]is not None:
                    row[19]=datetime.datetime.strptime(row[19], '%d/%m/%Y %H:%M:%S')
                cursor1.execute(sql,(row[0],row[1],row[2],row[4],row[6],row[7],row[9],row[10],row[11],row[12],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[22]))
                print("Cargando base de datos: "+str(int(((contador-1)/reader.line_num)))+'%'""", end="\r""")
                contador=contador+1
        conexion.commit()
        conexion.close()

def cargarDatosBogota():
    print("Descargando archivo de datos (Bogotá)")
    url = 'https://datosabiertos.bogota.gov.co/dataset/44eacdb7-a535-45ed-be03-16dbbea6f6da/resource/b64ba3c4-9e41-41b8-b3fd-2da21d627558/download/osb_enftransm-covid-19_23102020.csv'
    myfile = requests.get(url)
    open('datosCovidBogota.csv', 'wb').write(myfile.content)
    print("Archivo descargado satisfactoriamente")
def leerDatosBogota():
    print("Inicio de carga de datos")
    with open('datosCovidBogota.csv',newline='',encoding='latin-1') as File:
        reader = csv.reader(File,delimiter=';')
        conexion = tomarConexión()
        contador=0
        cursor1=conexion.cursor()
        sqlTable="drop table if exists datosBogota;"
        cursor1.execute(sqlTable)
        sqlTable="create table datosBogota("
        sqlTable+="id int auto_increment primary key,"
        sqlTable+="fecha_inicio_sintomas timestamp,"
        sqlTable+="fecha_diagnostico timestamp,"
        sqlTable+="ciudad varchar(20),"
        sqlTable+="localidad_asis varchar(50),"
        sqlTable+="edad int,"
        sqlTable+="sexo varchar(1),"
        sqlTable+="fuente_o_tipo_contagio varchar(30),"
        sqlTable+="ubicacion varchar(40),"
        sqlTable+="estado varchar(50));"
        cursor1.execute(sqlTable)
        for row in reader:
            if contador==0:
                contador=1
            elif contador+4>reader.line_num:
                continue
            else:
                sql="insert into datosBogota(fecha_inicio_sintomas,fecha_diagnostico,ciudad,localidad_asis,edad,sexo,fuente_o_tipo_contagio,ubicacion,estado) values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                for it in range(len(row)):
                    if str(row[it])=="":
                        row[it]=None
                try:   
                    if row[0]is not None:
                        row[0]=datetime.datetime.strptime(row[0], '%d/%m/%Y')
                        row[0] = row[0].strftime('%Y-%m-%d')
                    if row[1]is not None:
                        row[1]=datetime.datetime.strptime(row[1], '%d/%m/%Y')
                        row[1] = row[1].strftime('%Y-%m-%d')
                except:
                    continue
                cursor1.execute(sql,(row[0],row[1],row[2],row[3],row[4],row[6],row[7],row[8],row[9]))
                print("Cargando base de datos: "+str(int(((contador-1)/reader.line_num)))+'%'""",end="\r""")# int((i/reader.line_num))*100)
                contador+=1
        conexion.commit()
        conexion.close()

if __name__ == "__main__":
    #cargarDatosPais()
    #leerDatosPais()
    #cargarDatosBogota()
    leerDatosBogota()

