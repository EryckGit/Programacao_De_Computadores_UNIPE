#Construa um algoritmo que receba a altura e o peso de uma pessoa e calcule o Índice de Massa Corporal (IMC).

print("Calcule seu IMC com base no seu peso e altura")
peso = int(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

'''Calculo do IMC'''

imc = peso / (altura * altura)
print("O valor do seu imc é",imc)
