import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from main import tomarConexión
conexion=tomarConexión()
paleta=['#1abc9c','#ffdd33']
cursor=conexion.cursor()
#grafica N1 genero colombia
cursor.execute('select sexo,count(*) as cantidad from datos group by sexo;')
cantidad=[]
for fila in cursor:
    cantidad.append(fila[1])
sexo=['Femenino','Masculino']
colores=[paleta[0],paleta[1]]
print(cursor)
plt.title("Gráfica de contagios respecto género en Colombia")
plt.pie(cantidad, labels=sexo, colors=colores, startangle=90, explode=(0.01,0.01), radius=1.2, autopct='%1.2f%%' )
plt.show()

#grafica N2 genero departamentos
cursor.execute('select departamento, count(*) as contagios from datos group by departamento order by contagios desc, departamento limit 10;')
departamentos=[]
for fila in cursor:
    departamentos.append(fila[0])
cursor.execute('select departamento, sexo, count(*) as contagios from datos group by sexo, departamento order by contagios desc, departamento limit 20;')
masculino=[]
femenino=[]
for fila in cursor:
    if fila[1]=='M':
        masculino.append(fila[2])
    else:
        femenino.append(fila[2])
x=np.arange(len(departamentos))
#tamaño barra
width=0.20
#barra hombre
fig, ax = plt.subplots()
rectaMasc=ax.bar(x-width/2,masculino,width,label='Masculino')
#barra femenino
rectafem=ax.bar(x+width/2+0.1,femenino,width,label='Femenino')
#etiquetas
ax.set_ylabel('contagiados')
ax.set_title('Gráfica de contagiados por departamento según género')
ax.set_xticks(x)
ax.set_xticklabels(departamentos)
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

#Gráfica N3 edades en Colombia 
cursor = conexion.cursor(buffered=True)
cursor.execute('select edad, count(*) as contagiados from datos group by edad;')
edades=['1 a 20','21 a 40','41 a 60','61 a 80','Mayores a 80']

valores=[]

cursor.execute('select count(*) as contagiados from datos where edad between 1 and 20;')
for fila in cursor:
    valores.append(fila[0])

cursor.execute('select count(*) as contagiados from datos where edad between 21 and 40;')
for fila in cursor:
    valores.append(fila[0])

cursor.execute('select count(*) as contagiados from datos where edad between 41 and 60;')
for fila in cursor:
    valores.append(fila[0])

cursor.execute('select count(*) as contagiados from datos where edad between 61 and 80;')
for fila in cursor:
    valores.append(fila[0])   

cursor.execute('select count(*) as contagiados from datos where edad > 80;')
for fila in cursor:
    valores.append(fila[0])

fig, ax=plt.subplots()
#Etiqueta en el eje y
ax.set_ylabel('edades')
#Etiqueta en el eje x
ax.set_xlabel('Intervalos')
#Titulo
ax.set_title('Gráfica contagios por intervalos de edades en Colombia')

plt.bar(edades, valores)
plt.savefig('barras_simple.png')

plt.show()
conexion.close()