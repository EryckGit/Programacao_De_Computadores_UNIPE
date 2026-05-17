#Leia três números inteiros informados pelo usuário. Exiba em ordem decrescente o resto da divisão por 3.
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

divisao1 = numero1 % 3
divisao2 = numero2 % 3
divisao3 = numero3 % 3

if divisao1 >= divisao2 and divisao1 >= divisao3:
    if divisao2 >= divisao3:
        print(f"A ordem decrescente dos restos vai ser: {divisao1}, {divisao2}, {divisao3}")
    else:
        print(f"A ordem decrescente dos restos vai ser: {divisao1}, {divisao3}, {divisao2}")
elif divisao2 >= divisao1 and divisao2 >= divisao3:
    if divisao1 >= divisao3:
        print(f"A ordem decrescente dos restos vai ser: {divisao2}, {divisao1}, {divisao3}")
    else:
        print(f"A ordem decrescente dos restos vai ser: {divisao2}, {divisao3}, {divisao1}")
else:
    if divisao1 >= divisao2:
        print(f"A ordem decrescente dos resto vai ser: {divisao3}, {divisao1}, {divisao2}")
    else:
        print(f"A ordem decrescente dos resto vai ser: {divisao3}, {divisao2}, {divisao1}")