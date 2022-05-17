
datosPersonales = dict(
    nombre = 'Carlos', 
    edad = 25, 
    profesion = 'contador'
)
print(datosPersonales)

datosPersonales2 ={}
nombre1 = input('Digite el nombre\n')
datosPersonales2.setdefault('nombre',nombre1)
edad1 = int(input('Digite la edad:\n'))
datosPersonales2.setdefault('edad',edad1)
profesion1 = input('Digite la profesion\n')
datosPersonales2.setdefault('profesion',profesion1)

datosPersonales3 = {
    'nombre': nombre1,
    'edad': edad1,
    'profesion': profesion1
}

print(datosPersonales2)
print(datosPersonales3)

inventario={}
for i in range(4):
    codigo = int(input('Digite el código del articulo:\n'))
    cantidad = int(input('Digite la cantidad existente:\n'))
    inventario.setdefault(codigo,cantidad)  
    
print(inventario) 




