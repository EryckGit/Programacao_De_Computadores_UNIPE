#Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado.

valor = input("Digite um valor: ")


if valor >= "0" and valor <= "99999999999":
    valor = int(valor)
    print(valor*2)
else:
    print("Oque voce digitou não é numerico.")
