# Realice un ejercicio que lea n numeros enteros y nos diga cual
# es el mayor y el menor de ellos. 
# Datos de entrada->    n: cantidad de números
#                       numero: cada uno de los números ingresados por el usuario
# Datos de salida->     mayor: el mayor número
# Datos                 menor: el menor número

n = int(input("Digite la cantidad de numeros que desea ingresar\n"))
for i in range(n): # la variable i va a contar desde 0 hasta n-1
    numero = int(input(f"Digite el número {i+1}:\n"))
    if i == 0:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
print(f"El mayor de los {n} números ingresados es {mayor}")
print(f"El menor de los {n} números ingresados es {menor}")

    
 

