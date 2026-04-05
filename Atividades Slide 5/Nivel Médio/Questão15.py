#Leia um número e: Se estiver entre 10 e 20 → “Dentro”; Caso contrário → “Fora”

numero = int(input("Digite um número: "))

if numero >= 10 and numero <= 20:
    print(f"O número {numero} está Dentro entre 10 e 20.")    
else:
    print(f"O número {numero} está Fora entre 10 e 20.")    
