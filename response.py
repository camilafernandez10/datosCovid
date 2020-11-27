import mysql.connector
from mysql.connector import errorcode
import json
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from numpy.linalg import inv
from main import tomarConexión
from pandas import DataFrame
import math



def generarGraficas(data):
    conexion=tomarConexión()
    cursor=conexion.cursor()

    sql='set @total:=0;'
    cursor.execute(sql)
    sql='set @primerDia:=(select fecha_reporte_web from datos where municipio="'+data.get('municipio')+'" limit 1);'
    cursor.execute(sql)
    sql='select q1.fecha,q1.contagios, (@total:=@total+q1.contagios)as acumulado ,'
    sql +='(timestampdiff(day,@primerDia, q1.fecha)) as dia '
    sql+='from (select fecha_reporte_web as fecha,count(*)as contagios  from datos where municipio="'+data.get('municipio')+'" group by fecha_reporte_web ) as q1;'
    cursor.execute(sql)
    df = DataFrame(cursor.fetchall())
    t=df[3]; #días en número
    y=df[2]; #contagios
    y_dif=df[1] #contagios diarios

    pop=7.13e6
    newy=np.log(y/(pop-y))

    X = np.array([t,np.ones(len(t))]).T
    a = inv(X.T @ X) @ X.T @ newy 

    r=a[0]#r
    c=a[1]#c
    sol_predict = np.linspace(0, 250, num=len(t))
    contagios_predict = pop*np.exp(a[1]+a[0]*sol_predict)/(1+np.exp(a[0]+a[1]*sol_predict)) ### Modelo
    #fig = plt.figure()
    #plt.ion()
    #plt.scatter(t,y,label='Datos reales')

    #plt.xlabel('días'); plt.ylabel('Cantidad de casos detectados en '+data.get('municipio'));
    #plt.plot(sol_predict,contagios_predict,'c',label='Modelo')
    #plt.legend()
    nombre="Modelo de contagios.png"
    #plt.close(fig)
    #plt.savefig(nombre)

    #fig2=plt.figure()
    #plt.ion()
    sol_predict_deriv = np.linspace(0, 400, num=max(t))
    contagios_diarios=(r*pop*np.exp(r*sol_predict_deriv+c))/(1+np.exp(r*sol_predict_deriv+c))**2
    #plt.xlabel('días'); plt.ylabel('Posibles contagios diarios en '+data.get('municipio'));
    #plt.plot(sol_predict_deriv,contagios_diarios,label="modelo")
    #plt.plot(t,y_dif, label="Datos reales")
    #plt.legend()
    nombre2="Modelo de contagios diarios.png"
    #plt.close(fig2)
    #plt.savefig(nombre2)


    cursor.execute('select timestampdiff(day,@primerDia,"'+data.get('fecha')+'");')

    dias=cursor.fetchone()

    valor=(r*pop*np.exp(r*dias[0]+c))/(1+np.exp(r*dias[0]+c))**2
    texto=""
    if valor>0.005*pop:
        texto="No es seguro viajar"
    else:
        texto="Es seguro viajar"

    data = [{ 'nombre':"Contagios acumulados", 'link':nombre},{'nombre':"Contagios diarios",'link':nombre2},{texto:texto}]
    conexion.close()
    return data