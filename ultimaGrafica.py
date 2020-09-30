import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from main import tomarConexión
conexion=tomarConexión()
paleta=['#1abc9c','#ffdd33']
cursor=conexion.cursor()
cursor.execute('select atencion, count(*) as personas from datos group by atencion order by personas desc;')
atencion=[]
cantidad=[]
for fila in cursor:
    atencion.append(fila[0])
    cantidad.append(fila[1])
fig, ax = plt.subplots()

#Colocamos una etiqueta en el eje Y
ax.set_ylabel('Personas')
#Colocamos una etiqueta en el eje X
ax.set_xlabel('Estado')
#Título
ax.set_title('Estado actual de las personas')
#Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
plt.bar(atencion, cantidad)
plt.savefig('estadosPersonas.png')
#Finalmente mostramos la grafica con el metodo show()
plt.show()
conexion.close()
