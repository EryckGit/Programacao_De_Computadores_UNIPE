#Leia um número e informe: “Dentro do intervalo” se estiver entre 0 e 10; “Fora do intervalo” caso contrário.

print("Digite um número o qual o sistema irá informar se ele está dentro do intervalo entre 0 a 10 ou não!")
numero = int(input("Digite o número: "))

if numero >= 0 and numero <= 10:
    print("O seu número está dentro do intervalo!!")
else:
    print("O seu número está fora do intervalo!!")
