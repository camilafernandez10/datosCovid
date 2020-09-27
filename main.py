# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
def cargarDatos():
    url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD'
    myfile = requests.get(url)
    open('datosCovid.csv', 'wb').write(myfile.content)
#def leerDatos():
#    with open('datos.csv', newline='') as File:
#        reader = csv.reader(File)
#        for row in reader:
#            print(row)
cargarDatos()
#leerDatos()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cargarDatos()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
