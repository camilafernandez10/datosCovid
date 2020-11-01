import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from main import tomarConexión
conexion=tomarConexión()
paleta=['#1abc9c','#ffdd33']
cursor=conexion.cursor()
matplotlib.rc('xtick', labelsize=10) 
matplotlib.rc('ytick', labelsize=10) 

#Gráfica N1 por género colombia

cursor.execute('Select localidad_asis,count(*) as contagios from datosbogota where localidad_asis <> "Sin dato" and localidad_asis <> "Fuera de Bogotá" group by localidad_asis order by contagios desc limit 20;')
localidades=[]
for fila in cursor:
    localidades.append(fila[0])

#Femenino
cursor.execute('Select localidad_asis,count(*) as contagios from datosbogota where sexo = "F" group by localidad_asis order by contagios desc;')
femenino={}
for fila in cursor:
    femenino[fila[0]]=fila[1]

#Masculino
cursor.execute('Select localidad_asis,count(*) as contagios from datosbogota where sexo = "M" group by localidad_asis order by contagios desc;')
masculino={}
for fila in cursor:
    masculino[fila[0]]=fila[1]

#GÉNERO ORGANIZADO
masculino_organizado=[]
femenino_organizado=[]
for localidad in localidades:
    masculino_organizado.append(masculino[localidad])
    femenino_organizado.append(femenino[localidad])

width=0.2
#Gráfica
x=np.arange(len(localidades))
#barra hombre
fig, ax = plt.subplots(figsize=(13,7))
rectaMasc=ax.bar(x-width/2,masculino_organizado,width,label='Masculino')
#barra femenino
rectafem=ax.bar(x+width/2+0.15,femenino_organizado,width,label='Femenino')
#etiquetas
ax.set_ylabel('Contagiados',fontsize=14)
ax.set_title('Contagiados por localidades según género',fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(localidades,fontsize=9)
ax.set_xlabel('Localidades',fontsize=14)
#leyenda
ax.legend()
#funcion para agregar etiqueta a cada barra
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
#etiqueta a cada barra
autolabel(rectaMasc)
autolabel(rectafem)
fig.tight_layout()
plt.savefig('doble_barra.png')
plt.show()



#Gráfica N2 por edades

cursor = conexion.cursor(buffered=True)
cursor.execute('select edad, count(*) as contagiados from datosbogota group by edad;')
edades=['0 a 20','21 a 40','41 a 60','61 a 80','Mayores a 80']

valores=[]

cursor.execute('select count(*) as contagiados from datosbogota where edad between 0 and 20;')
for fila in cursor:
    valores.append(fila[0])

cursor.execute('select count(*) as contagiados from datosbogota where edad between 21 and 40;')
for fila in cursor:
    valores.append(fila[0])

cursor.execute('select count(*) as contagiados from datosbogota where edad between 41 and 60;')
for fila in cursor:
    valores.append(fila[0])

cursor.execute('select count(*) as contagiados from datosbogota where edad between 61 and 80;')
for fila in cursor:
    valores.append(fila[0])   

cursor.execute('select count(*) as contagiados from datosbogota where edad > 80;')
for fila in cursor:
    valores.append(fila[0])

fig, ax=plt.subplots(figsize=(10,5))
#Etiqueta en el eje y
ax.set_ylabel('Edades',fontsize=14)
#Etiqueta en el eje x
ax.set_xlabel('Intervalos', fontsize=14)
#Titulo
ax.set_title('Contagios por intervalos de edades en Bogotá',fontsize=18)

plt.bar(edades, valores)
plt.savefig('barras_edad.png')
plt.show()


#Gráfica N3 estado por localidad

cursor.execute('select localidad_asis,count(*) as contagios from datosbogota where localidad_asis <> "Sin dato" group by localidad_asis order by contagios desc;')
atencion=[]
cantidad=[]
for fila in cursor:
    atencion.append(fila[0])
    cantidad.append(fila[1])
fig, ax = plt.subplots(figsize=(10,5))

#Colocamos una etiqueta en el eje Y
ax.set_ylabel('Personas',fontsize=14)
#Colocamos una etiqueta en el eje X
ax.set_xlabel('Estado',fontsize=14)
#Título
ax.set_title('Estado actual de las personas en Bogotá',fontsize=18)
#Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
plt.bar(atencion, cantidad)
plt.savefig('barras_estado.png')
#Finalmente mostramos la grafica con el metodo show()
plt.show()
conexion.close()





