#Construa um algoritmo que receba a quantidade de horas trabalhadas por um funcionário e o valor da hora trabalhada, calculando o salário total.

print("Para calcular o salário do funcionário digite a quantidade de horas trabalhadas e o valor da hora.")
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = int(input("Digite a quantidade do valor por hora: "))

'''Calculo'''
salario = horas_trabalhadas * valor_hora
print("O salário que esse funcionário irá receber é =",salario)
