#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = ""
letra = ""
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("Numero de veces: ",contador)