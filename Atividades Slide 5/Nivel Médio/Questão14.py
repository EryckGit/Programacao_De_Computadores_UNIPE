#Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é múltiplo”.

valor = input("Digite um número: ")
valor = int(valor)

if valor % 3 == 0:
    print(f"O valor {valor} é Múltiplo de 3 e sua classe é {type(valor)}.")
else:
    print(f"O valor {valor} Não é Múltiplo de 3 e sua classe é {type(valor)}")
