#Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”.

numero = int(input("Digite um número: "))

if numero % 2 == 0 and numero >= 0:
    print("O numero digitado é Par Positivo!")
elif numero % 2 == 0 and numero < 0:
    print("O número digitado é Par Negativo!")
else:
    print("O número digitado é Impar!")
