#Construa um algoritmo que receba o valor de um produto e calcule o preço final considerando um acréscimo de 8% de imposto.

print("Diga o preço original do produto para ser adicionado os impostos: ")
valor = (float(input("Digite o valor do produto: ")))

'''Área de calculo'''

preco_final = valor * (1 + 0.08)
print("O preço final do seu produto é: R$",preco_final)
