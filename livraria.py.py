menu_principal = """
[Menu Principal Escolha uma das seguintes opções:
'1 - Categorias
'2 - Editoras
'3 - Autores
'4 - Livros
'0 - Sair do programa
"""

menu_autores = """
[Autores] Escolha uma das seguintes opções:
1 - Listar todos os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autoor por Id
0 - Voltar ao menu anterior
"""

tabela_autores = []

while True:
    print(menu_principal)
    opcao_principal = input('Digite a opção: ')

    if opcao_principal == '3':

        while True:
            print(menu_autores)
            opcao_autores = input('Digite a opção: ')
            if opcao_autores == '0':    
                break
            if opcao_autores == "1":
                if tabela_autores == []:
                    print("Nenhum Autor cadastrado.")
                else:
                    print("Id | Nome | Estilo | Pais")
                    for index, autor in enumerate(tabela_autores):
                        print(f'{index} | {autor[0]} | {autor[1]} | {autor[2]}')
            if opcao_autores == "2":
                nome_autor = input("Digite o nome do autor: ")
                estilo_autor = input("Digite o estilo do autor: ")
                pais_autor = input("Digite o país do autor: ")
                novo_autor = []
                novo_autor.append(nome_autor) 
                novo_autor.append(estilo_autor)
                novo_autor.append(pais_autor)
                tabela_autores.append(novo_autor)
                print("Autor adicionado com sucesso!")
            if opcao_autores =='3':
                id = int(input('Digite o id do Autor a ser excluido'))
                tabela_autores.pop(id)
                print('Autor excluído com sucesso!')

    if opcao_principal == "0":
        break

print('Programa Encerrado!')