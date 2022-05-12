# Realice un programa que lea los lados adyante y opuesto de un triángulo 
# rectángulo y nos devuelva el valor de la hipotenusa
#Para reordad matemática:
# P paréntesis      30 / 5 * 3 = 18, ok
# E exponente       4 * (5 + 3) = 32. ok
# M multiplicación*
# D división*
# A adición**
# S sustracción**
#Datos de entrada: a y b
#Datos de salida: h
def hipotenusa(a,b):
    h = (a**2 + b**2)**0.5
    return h
print(hipotenusa(3,4))


    


