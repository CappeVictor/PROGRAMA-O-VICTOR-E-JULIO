livros = [["Dom Casmurro", "Machado de Assis", "01", "03"],
           ["Harry Potter", "J.K.Rowling", "02", "07"],
           ["O Pequeno Principe", "Antoine de Saint-Exupéry", "03", "02"],
           ["A Hora da Estrela", "Clarice Lispector", "04", "08"],
           ["Vidas Secas", "Graciliano Ramos", "05", "04"],
           ["Sítio do Picapau Amarelo", "Monteiro Lobato", "05", "05"]]

usuario = [["Julio", "15", "01"],
           ["Victor", "15", "02"],
           ["Alisson", "34", "03"]]

while True:
           
           print("BIBLIOTECA")
           print("1 - Ver livros")
           print("2 - Cadastrar usuario")
           print("3 - Emprestar livro")
           print("4 - Encontrar usuario")
           print("5 - Livros disponiveis")
           print("6 - Ver usuarios")

           opcao = input("Escolha: ")
              
           if opcao == "1":
               print(f"{'Livro':<25} {'Autor':<25} {'Código':<10} {'Quantidade':>10}")
               for livro, autor, codigo, quantidade in livros:
                   print(f"{livro:<25} {autor:<25} {codigo:<10} {quantidade:>10}")
           
           elif opcao == "2":
               nome = input("Digite o seu nome de Usúario: ")
               idade = input("Digite a sua idade: ")
               id = int(input("Digite o seu id: "))
               for nome, idade, id in usuario:
                   ID = []
                   ID += id
               if id in ID:
                   print("ID ja usado, tente outro")
               else:
                   usuario += [nome, idade, id]
                   print("Usuario cadastrado")
           
           elif opcao == "3":
               livro = input("Digite o nome do livro: ")
               if livro in livros:
                   livros.remove(livro)
                   print("Livro emprestado.")
                   print("Livros restantes:")
                   print(livros)
               else:
                   print("Livro nao encontrado.")
           
           elif opcao == "4":
               id_teste = int(input("Digite o id do seu usuario: "))
               for nome, idade, id in usuario:
                       ID = []
                       ID += id
                       if id in ID:
                           print(nome, idade, id)
                           resposta = input("Este é o seu usuario?(S/N): ")
                           if resposta == "S":
                               print("Perfeito")
                           elif resposta == "N":
                               print("Tente novamente")
                           else:
                               print("Função Invalida")
           
           elif opcao == "5":
               print(f"{'Livro':<25} {'Quantidade':>10}")
               for livro, autor, codigo, quantidade in livros:
                   if int(quantidade) > 0:
                       print(f"{livro:<25} {quantidade:>10}")
           
           elif opcao == "6":
               print(f"{'Nome':<20} {'Idade':<10} {'ID':<10}")
               for nome, idade, id in usuario:
                   print(f"{nome:<20} {idade:<10} {id:<10}")
                   
           else:
               print("Opcao invalida.")
           livros = [["Dom Casmurro", "Machado de Assis", "01", "03"],
                      ["Harry Potter", "J.K.Rowling", "02", "07"],
                      ["O Pequeno Principe", "Antoine de Saint-Exupéry", "03", "02"]]
                      ["A Hora da Estrela", "Clarice Lispector", "04", "08"]
                      ["Vidas Secas", "Graciliano Ramos", "05", "04"]
                      ["Sítio do Picapau Amarelo", "Monteiro Lobato", "05", "05"]
           
           usuario = [["Julio", "15", "01"],
                      ["Victor", "16", "02"]
                      ["Alisson", "33", "03"]]
           
           print("BIBLIOTECA")
           print("1 - Ver livros")
           print("2 - Cadastrar usuario")
           print("3 - Emprestar livro")
           print("4 - Encontrar usuario")
           print("5 - Livros disponiveis")
           print("6 - Ver usuarios")
           print("7 - Sair")
           
           opcao = input("Escolha: ")
           
           if opcao == "1":
               print(f"{'Livro':<25} {'Autor':<25} {'Código':<10} {'Quantidade':>10}")
               for livro, autor, codigo, quantidade in livros:
                   print(f"{livro:<25} {autor:<25} {codigo:<10} {quantidade:>10}")
           
           elif opcao == "2":
               nome = input("Digite o seu nome de Usúario: ")
               idade = input("Digite a sua idade: ")
               id = int(input("Digite o seu id: "))
               for nome, idade, id in usuario:
                   ID = []
                   ID += id
               if id in ID:
                   print("ID ja usado, tente outro")
               else:
                   usuario += [nome, idade, id]
                   print("Usuario cadastrado")
           
           elif opcao == "3":
               livro = input("Digite o nome do livro: ")
               if livro in livros:
                   livros.remove(livro)
                   print("Livro emprestado.")
                   print("Livros restantes:")
                   print(livros)
               else:
                   print("Livro nao encontrado.")
           
           elif opcao == "4":
               id_teste = int(input("Digite o id do seu usuario: "))
               for nome, idade, id in usuario:
                       ID = []
                       ID += id
                       if id in ID:
                           print(nome, idade, id)
                           resposta = input("Este é o seu usuario?(Sim/Não): ")
                           if resposta == "Sim":
                               print("Perfeito")
                           elif resposta == "Não":
                               print("Tente novamente")
                           else:
                               print("Função Invalida")
           
           elif opcao == "5":
               print(f"{'Livro':<25} {'Quantidade':>10}")
               for livro, autor, codigo, quantidade in livros:
                   if int(quantidade) > 0:
                       print(f"{livro:<25} {quantidade:>10}")
           
           elif opcao == "6":
               print(f"{'Nome':<20} {'Idade':<10} {'ID':<10}")
               for nome, idade, id in usuario:
                   print(f"{nome:<20} {idade:<10} {id:<10}")
           
           elif opcao == "7":
                      print("saindo")
                      break

           else:
               print("Opcao invalida.")
