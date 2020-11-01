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

cursor.execute('select recuperado, count(*) as contagios from datosbogota group by recuperado;')
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

#MAPA DE CALOR BOGOTÁ
# use import geocoder

# get location data for large cities (latitude and longitude)
bosa = geocoder.osm('Localidad Bosa, Bogotá, Bogotá Distrito Capital')
barrios_unidos = geocoder.osm('Localidad Barrios Unidos, Bogotá, Bogotá Distrito Capital')
usaquen = geocoder.osm('Localidad Usaquén, Bogotá, Bogotá Distrito Capital')
chapinero = geocoder.osm('Localidad Chapinero, Bogotá, Bogotá Distrito Capital')
santa_fe = geocoder.osm('Localidad Santa Fe, Bogotá, Bogotá Distrito Capital')
san_cristobal = geocoder.osm('Localidad San Cristobal, Bogotá, Bogotá Distrito Capital')
fontibon = geocoder.osm('Localidad Fontibon, Bogotá, Bogotá Distrito Capital')
engativa = geocoder.osm('Localidad Engativa, Bogotá, Bogotá Distrito Capital')
kennedy = geocoder.osm('Localidad Kennedy, Bogotá, Bogotá Distrito Capital')
suba = geocoder.osm('Localidad Suba, Bogotá, Bogotá Distrito Capital')
teusaquillo = geocoder.osm('Localidad Teusaquillo, Bogotá, Bogotá Distrito Capital')
la_candelaria = geocoder.osm('Localidad La candelaria, Bogotá, Bogotá Distrito Capital')
martires = geocoder.osm('Localidad Martires, Bogotá, Bogotá Distrito Capital')
puente_aranda = geocoder.osm('Localidad Puente aranda, Bogotá, Bogotá Distrito Capital')
antonio_nariño = geocoder.osm('Localidad Antonio nariño, Bogotá, Bogotá Distrito Capital')
ciudad_bolivar = geocoder.osm('Localidad Ciudad Bolivar, Bogotá, Bogotá Distrito Capital')
usme = geocoder.osm('Localidad Usme, Bogotá, Bogotá Distrito Capital')
sumapaz = geocoder.osm('Localidad Sumapaz, Bogotá, Bogotá Distrito Capital')
rafael_uribe_uribe = geocoder.osm('Localidad Rafael Uribe Uribe, Bogotá, Bogotá Distrito Capital')
tunjuelito = geocoder.osm('Localidad Tunjuelito, Bogotá, Bogotá Distrito Capital')

#Consulta de datos Bogotá
cursor.execute('select localidad_asis,count(*) as contagios from datosbogota where localidad_asis <> "Sin dato" group by localidad_asis order by contagios desc;')
for fila in cursor:
    if fila[0]=="Bosa":
          bosa_latlng = [bosa.lat, bosa.lng, fila[1]/100]
    elif fila[0]=="Barrios Unidos":
          barrios_unidos_latlng = [barrios_unidos.lat, barrios_unidos.lng, fila[1]/100]
    elif fila[0]=="Usaquén":
          usaquen_latlng = [usaquen.lat, usaquen.lng, fila[1]/100]
    elif fila[0]=="Chapinero":
          chapinero_latlng = [chapinero.lat, chapinero.lng, fila[1]/100]
    elif fila[0]=="Santa Fe":  
          santa_fe_latlng = [santa_fe.lat, santa_fe.lng, fila[1]/100]
    elif fila[0]=="San Cristóbal":
          san_cristobal_latlng = [san_cristobal.lat, san_cristobal.lng, fila[1]/100]
    elif fila[0]=="Fontibón":        
          fontibon_latlng = [fontibon.lat, fontibon.lng, fila[1]/100]
    elif fila[0]=="Engativá":
          engativa_latlng = [engativa.lat, engativa.lng, fila[1]/100]
    elif fila[0]=="Kennedy":
          kennedy_latlng = [kennedy.lat, kennedy.lng, fila[1]/100]
    elif fila[0]=="Suba":        
          suba_latlng = [suba.lat, suba.lng, fila[1]/100]
    elif fila[0]=="Teusaquillo":
          teusaquillo_latlng = [teusaquillo.lat, teusaquillo.lng, fila[1]/100]
    elif fila[0]=="La Candelaria":        
          la_candelaria_latlng = [la_candelaria.lat, la_candelaria.lng, fila[1]/100]
    elif fila[0]=="Los Mártires":
          martires_latlng = [martires.lat, martires.lng, fila[1]/100]
    elif fila[0]=="Puente Aranda":
          puente_aranda_latlng = [puente_aranda.lat, puente_aranda.lng, fila[1]/100]
    elif fila[0]=="Antonio Nariño":
          antonio_nariño_latlng = [antonio_nariño.lat, antonio_nariño.lng, fila[1]/100]
    elif fila[0]=="Ciudad Bolívar":
          ciudad_bolivar_latlng = [ciudad_bolivar.lat, ciudad_bolivar.lng, fila[1]/100]
    elif fila[0]=="Usme":
          usme_latlng = [usme.lat, usme.lng, fila[1]/100]
    elif fila[0]=="Sumapaz":        
          sumapaz_latlng = [sumapaz.lat,sumapaz.lng, fila[1]/100]
    elif fila[0]=="Rafael Uribe Uribe":
          rafael_uribe_uribe_latlng = [rafael_uribe_uribe.lat,rafael_uribe_uribe.lng, fila[1]/100]  
    elif fila[0]=="Tunjuelito":
          tunjuelito_latlng = [tunjuelito.lat,tunjuelito.lng, fila[1]/100]  
# create list of cities with latitude, longitude, intensity
large_cities = [bosa_latlng, barrios_unidos_latlng, usaquen_latlng, chapinero_latlng, santa_fe_latlng, san_cristobal_latlng, fontibon_latlng,
               engativa_latlng,kennedy_latlng,  suba_latlng, teusaquillo_latlng, la_candelaria_latlng, martires_latlng, 
               puente_aranda_latlng, antonio_nariño_latlng, ciudad_bolivar_latlng, usme_latlng, sumapaz_latlng, rafael_uribe_uribe_latlng, tunjuelito_latlng]

map_heatmap = folium.Map([4.5988888, -74.08083], tiles='CartoDB Positron', zoom_start=11)

plugins.HeatMap(large_cities).add_to(map_heatmap)

map_heatmap



conexion.close()











