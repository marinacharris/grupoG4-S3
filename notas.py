#Realice un programa que convierta notas numéricas en porcentaje a letras,
#según la siguiente informacion:
# 0.0% - 59.99% -> D   
# 60.0% - 75.99% -> C
# 76.00% - 85.99% -> B
# 86.00% - 100% -> A 
# dato de entrada: nota numérica
# dato de salida: nota en letras

#operadores lógicos: and, or y not
# A     B       A and B     A or B 
# T     T          T           T 
# T     F          F           T
# F     T          F           T
# F     F          F           F

def convertir(nota):
    if nota >= 86.0 and nota <= 100.0:
        return("A")
    elif nota >= 76.0 and nota < 86.0:
        return f"B"
    elif nota >= 60.0 and nota < 76:
        return f"C"
    elif nota >= 0.0 and nota < 60:
        return f"D"
    else:
        return f'Por favor digite una nota entre 0 y 100'

respuesta="S"
while respuesta=='S' or respuesta =='s':
    try:    
        nota = float(input(f'Digite una nota entre 0 y 100\n'))
        print(convertir(nota))
    except:
        print(f'No se deben digitar letras o caracteres')
    finally: # se ejecuta independientemente de lo que ocurra en el try o en el except
        respuesta = input("Presione 'S' para continuar o cualquier letra para salir")