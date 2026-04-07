#Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo, e mostre na tela o valor

valor = int(input("Digite um número: "))

if valor >= 0 and valor <= 100:
  print(f"O número {valor} está entre 0 e 100")
else:
  print(valor)
