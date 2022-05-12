# Los diccionarios son estructuras de datos que se utilizan para 
# almacenar valores en pares clave-valor
# ejemplo->> 'nombre': 'Carlos'
# Son mutables
# Se puede decir son indexados por llave




datosPersonales = {
    "nombre": 'Carlos',
    'apellido': 'Gutiérrez',
    'email': 'cgutierrez@gmail.com',
    'edad': 45,
    'accesoAR': True,
    'dirección': 'Calle 20 58 99',
    'reconocimientos': {2019: False,2020: False,2021: True}
}
print(type(datosPersonales))
print(type(datosPersonales['reconocimientos']))
print(type(datosPersonales['edad']))
print(datosPersonales['dirección'])
# no se puede:  print(datosPersonales[5])

for i in datosPersonales:
    print(i)
    
for i in datosPersonales:
    print(datosPersonales[i])
    
print(datosPersonales)
    
datosPersonales['edad'] = 38
print("-------------------------------------")
print(datosPersonales)

print(datosPersonales.pop('dirección')) # elimina una llave
print(datosPersonales)
print("----------------------------------------------")
datosPersonales.setdefault('dirección','cra 5 89 20') #agrega una llave al final
print(datosPersonales)
