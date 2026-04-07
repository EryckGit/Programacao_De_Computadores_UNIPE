#Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 != numero2:
    if numero1 > numero2:
        print(f"A diferença entre esses dois números é: {numero1 - numero2}")
    else: 
        print(f"A diferença entre esses dois número é: {numero2 - numero1}")
else:
    print("Os dois números são iguais!")