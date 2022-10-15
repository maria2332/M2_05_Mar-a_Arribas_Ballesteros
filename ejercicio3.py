#ejercicio 3
contador = 0
while True:
    letra = input("Introduce una Letra: ")
    if letra == "a":
        contador += 1
    elif letra == ".":
        break
print("La letra 'a' se ha introducido", contador, "veces")