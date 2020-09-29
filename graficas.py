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
rectaMasc=ax.bar(x-width/2,masculino,width,label='masculino')
#barra femenino
rectafem=ax.bar(x+width/2+0.01,femenino,width,label='femenino')
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
conexion.close()