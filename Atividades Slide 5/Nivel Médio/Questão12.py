#Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

'''Poderia declara antes a variável resultado mas prefiri assim para escrever mais e praticar mais'''

if numero1 > numero2:
    resultado = numero1 + numero2
    print("O maior numero é o",numero1,"e a soma entre eles é igual a:",resultado)
elif numero2 > numero1:
    resultado = numero2 + numero1
    print("O maior número é o",numero2,"E a soma entre eles é igual a:",resultado)
else:
    resultado = numero1 + numero2
    print("Os números são iguais e a soma entre eles é:",resultado)
