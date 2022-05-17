# Es una estructura de datos que se utilizan para almacenar valores 
# de la forma llave-valor, ejemplo 'Nombre':'Carlos'
# Los diccionarios son indexados a traves de una llave
# Los diccionarios son mutables


datosPersonales = {
    'Nombre':'Carlos',
    'Apellido': 'Gutiérrez', 
    'edad': 30,
    'casado': True,
    'ventas': {
        1:10,
        2:30,
        3:2,
        4:15
    }  
}
datosPersonales['casado'] = False
datosPersonales['ventas'][3] = 5
print(datosPersonales)
print(type(datosPersonales), type(datosPersonales['casado']))
print(datosPersonales['ventas'][3])

for i in datosPersonales: # i toma los valores de las llaves
    print(i)

for i in datosPersonales:
    print(datosPersonales[i])