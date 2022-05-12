# Las listas son una estructura de datos y se utilizan para guardar 
# varios elementos en una sola variable
# Las listas son mutables
# Las son indexadas
# Pueden almacenar datos de distintos tipos en una sola lista

MarcasCarros = ['Nissan', 'Audi', 'Chevrolet', 'Renault']
datosPersonales = list(('Juan', 45, False, [5,8,3]))
print(type(datosPersonales),type(datosPersonales[2]))

print(MarcasCarros)
print(datosPersonales)
print(MarcasCarros[1])

for i in MarcasCarros:
    print(i)
    
MarcasCarros[0]='Toyota'
print(MarcasCarros)