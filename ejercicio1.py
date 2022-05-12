# Realice un programa que lea el código de un producto como llave de un 
# diccionario y en dicha llave va a almacenar nombre, precio y cantidad 
# del producto en una lista.
# El programa debe permitir cargar datos al diccionario, debe mostrar 
# un listado completo del diccionario y debe permitir consultar un producto 
# por su llave.
def prueba():
    pass

def crear(productos):
    codigo = int(input('Ingrese el codigo del producto\n'))
    nombre = input('Ingrese el nombre del producto\n')
    precio = int(input('Ingrese el precio del producto\n'))
    cantidad = int(input('Igrese el cantidad del producto\n'))
    productos.setdefault(codigo,[nombre,precio,cantidad])
    return productos
    
def mostrar(productos):
    print('Listado de Productos')
    for i in productos:
        print(i, productos[i][0], productos[i][1], productos[i][2])
    
def consultar(productos):
    cod = int(input ('Ingrese el cod del producto\n'))
    if cod in productos:
        print(productos[cod][0], productos[cod][1], productos[cod][2])
    
   

continuar = 's'
productos = {}
while continuar =='s' or continuar == 'S':
    print('MENU')
    print('1. Crear producto')
    print('2. Mostar producto')
    print('3. Consultar')
    opcion = int(input(f'Digite una de las tres opciones [1,2,3]\n'))
    if opcion == 1:
        crear(productos)
        print('Producto creado')
    elif opcion == 2:
        mostrar(productos)
    elif opcion == 3:   
        consultar(productos)
    else:
        print('Digita una opción válida')
    continuar = input('Presione "s" para continuar o cualquier letra para salir')
    
        
