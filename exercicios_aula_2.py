# 1) Entrar via teclado com a base e a altura de um retângulo, calcular e exibir sua área.
# Fórmula: base * altura

# base = int(input("Digite a base do retângulo: "))
# altura = int(input("Digite a altura do retângulo: "))

# area = base * altura

# print(f"A área do triângulo é {area}")


# 2) Calcular e exibir a média aritmética de quatro valores quaisquer que serão digitados.
# Resolvam usando duas abordagens
# 2.1) sem 'for'

# num1 = int(input("Digite o primeiro valor: "))
# num2 = int(input("Digite o segundo valor: "))
# num3 = int(input("Digite o terceiro valor: "))
# num4 = int(input("Digite o quarto valor: "))

# media = (num1 + num2 + num3 + num4)/4

# print(f"A média aritmética dos valores é: {media}")

# 2.2) com 'for' ou 'while'
# valor = 0
# for num in range (1,5):
#     num = int(input("Digite o valor: "))
#     valor = num + valor
# media = valor/4
# print(f"A média aritmética é: {media}")

# 3) Calcular e exibir a área de um retângulo, a partir dos valores da base e altura que serão digitados. Se a área for maior que 100, exibir a mensagem “Terreno grande”, caso contrário, exibir a mensagem “Terreno pequeno”.
base = int(input("Digite a largura do terreno: "))
altura = int(input("Digite a comprimento do retângulo: "))

area = base * altura
print(f"A área do terreno é: {area}")

if area > 100:
    print("Terreno grande")
else:
    print("Terreno pequeno")