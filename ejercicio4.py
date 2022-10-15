#ejercicio 4
palabra1 = input("Introduce una palabra: ")
palabra2 = input("Introduce una palabra: ")
palabra3 = input("Introduce una palabra: ")

lista = (palabra1, palabra2, palabra3)

print (lista [0], len(palabra1))
print (lista [1], len(palabra2))
print (lista [2], len(palabra3))

while True:
  if len(palabra1) > len (palabra2) and len(palabra1) > len (palabra3):
    print ("La palabra con mas caracteres fue la palabra 1")
  elif len(palabra2) > len (palabra1) and len(palabra2) > len (palabra3):
    print ("La palabra con mas caracteres fue la palabra 2")
  else:
    print ("La palabra con mas caracteres fue la palabra 3")
  break 