#Leia um valor informado pelo usuário. Exiba o tipo da variável lida. Verifique se é possível converter o valor para número real (float). Se for possível, exiba o resultado da divisão desse número por 2. Caso contrário, exiba: “Não numérico”.
valor = input("Digite um valor: ")

if valor >= "0" and valor <= "99999999999999999999999999":
    valor = float(valor)
    print(f"Esse valor dividido por 2 é igual a: {valor/2}")
    print(type(valor))
else:
    print(type(valor))
    print("Não é numerico!")