#Leia dois números e exiba qual é o maior.

print("Digite dois números e o sistema irá decidir qual ou maior ou o menor!")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O número maior é:",numero1)
elif numero2 > numero1:
    print("O número maior é:",numero2)
else:
    print("Os dois número são iguais!")
