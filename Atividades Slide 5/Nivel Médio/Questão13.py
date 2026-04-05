#Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro.

numero = int(input("Digite um número: "))

if numero > 100:
    print(f"A metade {numero} é {numero / 2}.")
else:
    print(f"O dobro de {numero} é {numero * 2}.")
