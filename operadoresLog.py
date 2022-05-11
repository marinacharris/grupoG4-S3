#Realizar un programa que indique si una persona debe presentar 
#la declacion de renta. Las condiciones para presentar este impuesto son:
#Ser mayor de edad y
#Tener ingresos anuales superiores o iguales a $50.831.000

def renta(edad, ingresos):
    if edad >= 18 and ingresos >= 50831000:
        return f'Usted debe declarar renta'
    else:
        return f'Usted no debe declarar renta'

def renta2(edad, ingresos):
    if edad <18 or ingresos < 50831000:
        return f'Usted no debe declarar renta'
    else:
        return f'Usted debe declarar renta'
    
    
print(renta(25, 60000000))
print(renta(17, 60000000))
print(renta(25, 40000000))
print(renta(17, 0))
print("-----------------------")
print(renta2(25, 60000000))
print(renta2(17, 60000000))
print(renta2(25, 40000000))
print(renta2(17, 0))
