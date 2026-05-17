#Leia um valor informado pelo usuário. Tente convertê-lo para número inteiro. Caso não seja possível realizar a conversão, exiba: “Entrada inválida”. Caso a conversão seja bem-sucedida: Se o número for maior que 10, exiba: “Alto”. Caso contrário, exiba: “Baixo”.

valor = (input("Digite um valor: "))

if valor >= "0" and valor <= "999999999999999999999999999999":
    valor = int(valor)
    if valor > 10:
        print("Alto")
    else:
        print("Baixo")
else:
    print("Entrada invalida.")