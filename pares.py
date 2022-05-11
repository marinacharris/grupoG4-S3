#operación matemática módulo, devuelve el residuo de una división de la
#ejemplo: 8%3 = 2, 8%4 = 0
#Realice un programa que lea un numero entero y diga si es par o impar
#20%2 = 0, 15%2 = 1, 33%2 = 1, 10%2 = 0

numero = int(input('Digite un número entero:\n'))
if numero%2 == 0:
    print("El número es par")
else:
    print("El número es impar")