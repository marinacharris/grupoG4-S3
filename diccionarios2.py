datosPersonales = dict(nombre = 'Juan',edad = 25, direccion ='Av 20 1518')
print(datosPersonales)
#copy, copia los archivos
diccionario2 = datosPersonales.copy()
print(diccionario2)
# método clear, borra todo el diccionario
datosPersonales.clear()
print(datosPersonales)
datosPersonales.setdefault('nombre', 'Sofía')
print(datosPersonales)
print(datosPersonales.get('nombre')) # get obtiene el valor de una llave
print(datosPersonales.values())
print(datosPersonales.keys())
