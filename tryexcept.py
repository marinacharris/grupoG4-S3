try:
    num = int(input('Digite un numero entero:\n'))
    print(num)
#   print(x)
    
except ValueError:
    print('digite solo números')

except NameError:
    print('Por favor escriba bien su código')