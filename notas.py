#Realice un programa que convierta notas numéricas en porcentaje a letras,
#según la siguiente informacion:
# 0.0% - 59.99% -> D
# 60.0% - 75.99% -> C
# 76.00% - 85.99% -> B
# 86.00% - 100% -> A 
# dato de entrada: nota
# dato de salida: letra

def nota_letra(nota):
    if nota >= 0 and nota < 60:
        return f"la calificación en letra es D"
    elif nota >= 60 and nota < 76:
        return f"La calificación en letra es C"
    elif nota >= 76 and nota < 86:
        return f"La calificación en letra es B"
    elif nota >= 86 and nota <= 100:
        return f"La calificación en letra es A"
    else: 
        return f"Por favor digite una nota entre 0 y 100"
    
        
try:
    nota = float(input("Digite una nota entre 0 y 100\n"))
    print(nota_letra(nota))
except:
    print("Usted debe digitar solamente números, no se permiten letras ni caracteres especiales")