#Leia um número inteiro. Verifique se ele está no intervalo de 1 a 100 (inclusive). Se estiver: Verifique se o número é par ou ímpar; Exiba: “Par no intervalo” ou “Ímpar no intervalo”. Caso não esteja no intervalo, exiba: “Fora do intervalo”

numero = int(input("Digite um numero inteiro: "))

if numero >= 1 and numero <= 100:
    if numero % 2 == 0:
        print("Par no intervalo")
    else:
        print("Impar no intervalo")
else:
    print("Fora do intervalo")