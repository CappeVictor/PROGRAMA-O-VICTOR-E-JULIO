import os
def ver_livros():
    os.system('cls')
    print(f"{'Livro':<40} {'Autor':<25} {'Código':<10} {'Quantidade':<12}")
    for livro, autor, codigo, quantidade in livros:
        print(f"{livro:<40} {autor:<25} {codigo:<10} {quantidade:<12}")
 
def garantir_usuario(id_usuario):
    for nome, idade, ide in usuario:
        if ide == id_usuario:
            return
    print("Usuario nao encontrado, cadastro necessario.")
    nome = input("Digite o seu nome de Usuario: ")
    idade = input("Digite a sua idade: ")
    while not idade.isdigit():
        print("Idade invalida, digite somente numeros.")
        idade = input("Digite a sua idade: ")
    usuario.append([nome, idade, id_usuario])
    print("Usuario cadastrado")
 
def cadastrar_usuario():
    os.system('cls')
    nome = input("Digite o seu nome de Usúario: ")
    idade = input("Digite a sua idade: ")
    while not idade.isdigit():
        print("Idade invalida, digite somente numeros.")
        idade = input("Digite a sua idade: ")
    id_usuario = input("Digite o seu id: ")
    while True:
        ID = []
        for nomes, idades, ide in usuario:
            ID.append(ide)
        if id_usuario in ID:
            print("ID ja usado, tente outro")
            id_usuario = input("Digite o seu id: ")
        else:
            usuario.append([nome, idade, id_usuario])
            print("Usuario cadastrado")
            break
 
def emprestar_livro():
    os.system('cls')
    id_usuario = input("Digite o seu id de usuario: ")
    garantir_usuario(id_usuario)
    livro = input("Digite o nome do livro: ").upper()
    encontrado = False
    for i in range(len(livros)):
        if livro == livros[i][0]:
            encontrado = True
            if int(livros[i][3]) > 0:
                livros[i][3] = str(int(livros[i][3]) - 1)
                print("Livro emprestado.")
                print("Livros restantes: ", end="")
                print(livros[i][3])
            else:
                print("Livro indisponível.")
            break
    if not encontrado:
        print("Livro nao encontrado.")
 
def devolver_livro():
    os.system('cls')
    id_usuario = input("Digite o seu id de usuario: ")
    garantir_usuario(id_usuario)
    livro = input("Digite o nome do livro: ").upper()
    encontrado = False
    for i in range(len(livros)):
        if livro == livros[i][0]:
            encontrado = True
            quantidade_anterior = int(livros[i][3])
            if quantidade_anterior + 1 > int(estoque_maximo[i]):
                print("Quantidade maxima do livro atingida, devolucao nao realizada.")
            else:
                livros[i][3] = str(quantidade_anterior + 1)
                print("Livro devolvido.")
                print()
                print("Relatório de devolução")
                print(f"Livro: {livros[i][0]}")
                print(f"Autor: {livros[i][1]}")
                print(f"Código: {livros[i][2]}")
                print(f"Quantidade de livros antes: {quantidade_anterior}")
                print(f"Quantidade de livros depois: {livros[i][3]}")
            break
    if not encontrado:
        print("Livro nao encontrado.")
 
def encontrar_usuario():
    os.system('cls')
    tentar_novamente = True
    while tentar_novamente:
        tentar_novamente = False
        id_teste = input("Digite o id do seu usuario: ")
        ID = []
        for nome, idade, ide in usuario:
            ID.append(ide)
        if id_teste in ID:
            for nome, idade, ide in usuario:
                if id_teste == ide:
                    print(nome, idade, ide)
                    resposta = input("Este é o seu usuario?(S/N): ")
                    if resposta.upper() == "S":
                        print("Perfeito")
                    elif resposta.upper() == "N":
                        print("Tente novamente")
                        tentar_novamente = True
                    else:
                        print("Função Invalida")
                    break
        else:
            print("ID nao encontrado.")
 
def livros_disponiveis():
    os.system('cls')
    print(f"{'Livro':<25} {'Quantidade':>10}")
    for livro, autor, codigo, quantidade in livros:
        if int(quantidade) > 0:
            print(f"{livro:<25} {quantidade:>10}")
 
def ver_usuarios():
    os.system('cls')
    print(f"{'Nome':<20} {'Idade':<10} {'ID':<10}")
    for nome, idade, ide in usuario:
        print(f"{nome:<20} {idade:<10} {ide:<10}")
 
def sair():
    os.system('cls')
    print("Saindo do programa...")
 
livros = [["CURSO INTENSIVO DE PYTHON", "ERIK MATTHES", "01", "03"],
["AUTOMATIZE TAREFAS MAÇANTES COM PYTHON", "AL SWEIGART", "02", "04"],
["PYTHON FLUENTE", "LUCIANO RAMALHO", "03", "02"],
["CÓDIGO LIMPO", "ROBERT C. MARTIN", "04", "05"],
["O PROGRAMADOR PRAGMÁTICO", "DAVID THOMAS", "05", "03"],
["ESTRUTURAS DE DADOS E ALGORITMOS", "ROBERT LAFORE", "06", "04"]]      
 
estoque_maximo = []
for livro, autor, codigo, quantidade in livros:
    estoque_maximo.append(quantidade)
 
usuario = [["Julio", "15", "01"],
["Victor", "16", "02"],
["Alisson", "34", "03"],
["Marcio", "50", "04"],
["Renato", "54", "05"]]
 
while True:
    print("BIBLIOTECA")
    print("1 - Ver livros")
    print("2 - Cadastrar usuario")
    print("3 - Emprestar livro")
    print("4 - Encontrar usuario")
    print("5 - Livros disponiveis")
    print("6 - Ver usuarios")
    print("7 - Devolver livro")
    print("8 - Sair")
    opcao = input("Escolha: ")
 
    if opcao == "1":
        ver_livros()
 
    elif opcao == "2":
        cadastrar_usuario()
 
    elif opcao == "3":
        emprestar_livro()
 
    elif opcao == "4":
        encontrar_usuario()
 
    elif opcao == "5":
        livros_disponiveis()
 
    elif opcao == "6":
        ver_usuarios()
 
    elif opcao == "7":
        devolver_livro()
 
    elif opcao == "8":
        sair()
        break
 
    else:
        print("Opcao invalida.")
 
