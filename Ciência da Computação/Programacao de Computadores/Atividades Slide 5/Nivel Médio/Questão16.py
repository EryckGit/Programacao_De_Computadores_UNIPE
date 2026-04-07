#Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado.

valor = input("Digite um valor: ")
print(type(valor))

'''.isdigit() serve para descrobrir se oque pessoa escreveu é númerico'''

if valor.isdigit():      
    valor = int(valor)
    print(valor * 2)
else:
    print(False)