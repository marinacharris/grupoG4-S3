try:
    numero = int(input("Digite un número:\n"))
    print(numero)
    #print(x)
except ValueError:
    print("Usted debe digitar solamente números, no se permiten letras ni caracteres especiales")
except NameError:
    print("Por favor declare todas las variables")   
