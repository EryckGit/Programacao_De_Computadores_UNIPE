#Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
  if numero > 0:
    print("par positivo!")
  elif numero < 0:
    print("par negativo!")
  else:
    print("neutro")
else:
  if numero > 0:
    print("impar positivo!")
  else:
    print("impar negativo!")
  

