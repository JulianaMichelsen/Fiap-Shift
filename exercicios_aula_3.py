# Aula 03, Exercício 01
# Entrar via teclado com o valor de uma temperatura em graus Celsius, calcular e exibir sua temperatura equivalente em Fahrenheit.
# Fórmula: F = (C * 1.8) + 32
# Obs.: ao imprimir o resultado usem o f-string para formatar a mensagem.
temperatura_c = float(input("Digite a temperatura em graus Celsius: "))
temperatura_f = (temperatura_c*1.8)+32
print(f"A temperatura em Fahrenheite é: {temperatura_f}")

# Aula 03, Exercício 02
# Criar um programa para analisar a velocidade de um automóvel.
# Solicitar via teclado os valores da aceleração (a em m/s2), velocidade inicial (v0 em m/s) e o tempo de percurso (t em s).
# Calcular e exibir a velocidade final do automóvel em km/h. E exibir uma mensagem de acordo com a tabela abaixo:
# V <= 40 -> Veículo muito lento
# 40 < V <=60 -> Velocidade permitida
# 60 < V <= 80 -> Velocidade de cruzeiro
# 80 < V <= 120 -> Veículo rápido
# V > 120 -> Veículo muito rápido
# Fórmula para o cálculo da velocidade em km/h: velocidade final = (velocidade inicial + (a * t)) * 3.6
# Obs.: ao imprimir o resultado usem o f-string para formatar a mensagem.

aceleracao = (int(input("Digite a aceleração em m/s: ")))
velocidade_inicial = (int(input("Digite a velocidade inicial em m/s: ")))
tempo = (int(input("Digite o tempo de percurso inicial em s: ")))
velocidade_final = (velocidade_inicial + (aceleracao * tempo)) * 3.6

if velocidade_final <=40:
    print(f"A velocidade final foi: {velocidade_final}")
    print("Veículo muito lento.")
elif velocidade_final > 40 and velocidade_final <= 60:
    print(f"A velocidade final foi: {velocidade_final}")
    print("Velocidade permitida.")
elif velocidade_final > 60 and velocidade_final <= 80:
    print(f"A velocidade final foi: {velocidade_final}")
    print("Velocidade de cruzeiro.")
elif velocidade_final > 80 and velocidade_final <= 120:
    print(f"A velocidade final foi: {velocidade_final}")
    print("Veículo rápido.")
else:
    print(f"A velocidade final foi: {velocidade_final}")
    print("Veículo muito rápido.")

# Aula 03, Exercício 03
# Entrar via teclado com dois valores numéricos quaisquer. Após isso, exibir um seletor de opções (“menu”) com as seguintes opções:
# Adição
# Divisão
# Multiplicação
# Subtração
# Sair do programa
# Solicitar uma opção para o usuário e processar a respectiva operação.
# Se o usuário digitar o número 5 mostrar uma mensagem de finalização e sair do programa.
# Mostrar mensagem de erro se a opção escolhida não existir no menu e sair do programa.
# Repare que a opção de número dois é de divisão. Se o denominador for zero o programa deverá 1) mostrar uma mensagem de erro e depois 2) sair do programa.
menu = """
[Menu] Escolha uma das seguintes opções:
1 - Adição
2 - Divisão
3 - Multiplicação
4 - Subtração
0 - Sair do programa
"""

while True:
    print("Escolha dois números inteiros!")
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    print(menu)
    print()
    opcao = input('Digite a opção: ')
    match opcao:
        case '0':
            break
        case '1':
            adicao = (num1+num2)
            print("Você escolheu adição.")
            print(f"O resultado da adição. é {adicao}")

        case '2':
            if num1 == 0 or num2 == 0:
                print("Não é possível realizar divisão por 0!")
                break
            else:
                divisao = (num1 / num2)
                print("Você escolheu divisão.")
                print(f"O resultado da divisão. é {divisao}")

        case '3':
            multiplicacao = (num1 * num2)
            print("Você escolheu multiplicação.")
            print(f"O resultado da amultiplicação. é {multiplicacao}")

        case '4':
            subtracao = (num1-num2)
            print("Você escolheu subtração.")
            print(f"O resultado da subtração. é {subtracao}")

        case _:
            print("Número inválido")
            break
print("Programa encerrado!")



        
    
# Aula 03, Exercício 04

# Entrar com dois números inteiros via teclado, onde o segundo deverá ser maior que o primeiro. Repetir a operação de leitura do segundo número enquanto a regra não for respeitada.

while True: 
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite um número maior que o primeiro: "))
    if num1 >= num2:
        num2 = int(input("Digite um número maior que o primeiro"))
    else:
        print("Parabéns!")
        break


