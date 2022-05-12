# Realice un programa que lea n números enteros y diga cuál es el mayor
# número y cuál es el menor número
# Datosde entrada-> n: cantidad de números
#                   numero: cada número que va ingresando el usuario
# Datos de salida-> mayor: el mayor número
#                   menor: el menor número
n = int(input("Digite la cantidad de números que desea ingresar\n"))
for i in range(1,n+1):
    numero = int(input(f"Digite el número {i}\n"))
    if i == 1:
        mayor = numero
        menor = numero 
    else: 
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
print(f"El mayor de los {n} numeros ingresados es {mayor}")
print(f"El menor de los {n} numeros ingresados es {menor}")
    
      
    
    
    

