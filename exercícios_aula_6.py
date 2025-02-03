# Aula 06 - Exercício 04

# Dadas essas duas listas:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# Crie um programa para alterar a list1 de forma a incorporar a sub_list para que o resultado seja este:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1[2][1][2].extend(sub_list)

print(list1)
 
# Aula 06 - Exercício 05

# Crie uma função que retorne uma letra do alfabeto dado um índice numérico. Por exemplo, um índice de 1 deve retornar "A", um índice de 3 deve retornar "C", e assim por diante.

# Números além do intervalo do alfabeto devem retornar uma string vazia.

def letra_por_indice(indice):
    if 1 <= indice <= 26:
        return chr(64 + indice) 
    else:
        return ""
    
print(letra_por_indice(1))  # Retorna "A"
print(letra_por_indice(3))  # Retorna "C"
print(letra_por_indice(27))  # Retorna "
 
# Aula 06 - Exercício 06

# Escreva uma função Python que receba uma string como entrada e retorne um dicionário contendo o número de caracteres maiúsculos e minúsculos na string. Quaisquer caracteres que não possam ser categorizados como maiúsculos ou minúsculos (por exemplo, símbolos) devem ser contados como "outros".

def contar_caracteres(string):
    contagem = {'maiúsculos': 0, 'minúsculos': 0, 'outros': 0}
    
    for char in string:
        if char.isupper():
            contagem['maiúsculos'] += 1
        elif char.islower():  
            contagem['minúsculos'] += 1
        else:  
            contagem['outros'] += 1
    
    return contagem

# Exemplo de uso
resultado = contar_caracteres("Hello World! 123")
print(resultado)

# Aula 06 - Exercício 07

# Crie uma função que recebe uma string (palavra ou texto) como argumento e retorna o caractere mais comum nessa string.

from collections import Counter

def caractere_mais_comum(string):
    contador = Counter(string)
    
    return contador.most_common(1)[0][0]

resultado = caractere_mais_comum("exemplo de texto")
print(resultado)
 
# Aula 06 - Exercício 08

# Escreva uma função que recebe como argumento uma string cujo valor é um endereço de e-mail e retorna Verdadeiro/Falso dependendo se é um endereço de e-mail válido.

# Regras:

# * Deve começar com uma letra ou um número

# * Deve conter um símbolo @

# * Deve conter pelo menos 1 caractere antes do símbolo arroba

# * Deve ter pelo menos 1 caractere depois do símbolo @ e antes do ponto(.)

# * Deve conter pelo menos 1 caractere depois do último ponto(.)

# * Máximo de 256 caracteres

import re

def validar_email(email):

    padrao = r"^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,}$"
    
    if len(email) > 256:
        return False

    return bool(re.match(padrao, email))

emails_teste = [
    "usuario@email.com",   
    "1usuario@email.com",    
    "@email.com",           
    "usuario@.com",         
    "usuario@email.",        
    "usuario@.com.br",      
    "usuario@emailcom",      
    "usuário@email.com",     
    "u" * 257 + "@email.com" 
]

for email in emails_teste:
    print(f"{email}: {validar_email(email)}")