#ejercicio 2
numero1 = int(input("Introduzca un numero: "))
numero2 = int(input("Introduzca un numero: "))
numero3 = int(input("Introduzca un numero: "))

lista = (numero1,numero2,numero3)
while True:
  if (numero1 == 0):
    print("error")
  elif (numero1 < numero2 < numero3):
    print("Estan en orden ascendente")
  else:
    print("No estan en orden ascendente")
  break 
print (lista) 