# las cadenas son indexadas de forma numérica
# las cadenas son inmutables
lenProg = "Python"
print(lenProg[3])
print(lenProg[-1])
lenProg = "Java es genial"
print(lenProg)
# lenProg[0]='p', esto NO se puede, las cadenas son inmutables
print(len(lenProg))
print(lenProg[4])
cadenaVacia=""
print(len(cadenaVacia))
print(lenProg.count('a'))
fruta = 'manzana'
print(fruta[2:5])
print(fruta[:5])
print(fruta[2:])
print(fruta[2:5:2])
print(fruta.replace('man', 'tab'))
print(fruta)

for i in fruta: # la variable i va tomando los valores de los carateres de fruta
    print(i)



