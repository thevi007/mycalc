def multiplicacao():
    num1 = float(input("Digite um numero : "))
    num2 = float(input("Digite outro numero : "))
    return num1 * num2

def divisao():
    num1 = float(input("Digite um numero : "))
    num2 = float(input("Digite outro numero : "))
    return num1 / num2

def soma():
    num1 = float(input("Digite um numero : "))
    num2 = float(input("Digite outro numero : "))
    return num1 + num2

def subtracao():
    num1 = float(input("Digite um numero : "))
    num2 = float(input("Digite outro numero : "))
    return num1 - num2

operacao = input("Escolha uma das seguintes operações : +,-,*,/  :   ")
resultado = 0

if(operacao == "+"):
    operacao = "soma"
    resultado = soma()

elif(operacao == "-"):
    operacao = "subtração"
    resultado = subtracao()

elif(operacao == "*"):
    operacao = "multiplicação"
    resultado = multiplicacao()

elif(operacao == "/"):
    operacao = "divisão"
    resultado = divisao()

else:
    print("selecione uma opção valida")

print(f"o resultado da {operacao} foi {resultado}")

