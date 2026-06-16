import os
import datetime
import pickle

pedidos = {}
try:
   arq_pedidos = open("pedidos.dat", "rb")
   pedidos = pickle.load(arq_pedidos)
except:
   arq_pedidos = open("pedidos.dat", "wb")
arq_pedidos.close()


clientes = {}
try:
   arq_clientes = open("clientes.dat", "rb")
   clientes = pickle.load(arq_clientes)
except:
   arq_clientes = open("clientes.dat", "wb")
arq_clientes.close()


produtos = {}
try:
   arq_produtos = open("produtos.dat", "rb")
   produtos = pickle.load(arq_produtos)
except:
   arq_produtos = open("produtos.dat", "wb")
arq_produtos.close()



# pedidos = {
    # número do pedido : [cliente, produto, [quantidade], data]
# }

# clientes = {
    # nome da empresa : [razão social, cnpj, telefone de contato, localização com UF]
# }

# produtos = {
    # nome do produto : [preço, quantidade em estoque, código de identificação]
# }



resp = ''
while resp != '0':
    os.system('cls' if os.name == 'nt' else 'clear')

    print("############################################")
    print("######       Gentildonna's Attelier       ######")
    print("############################################")
    print()
    print("#####      1 - Módulo Cliente            #####")
    print("#####      2 - Módulo Produto        #####")
    print("#####      3 - Módulo Pedido            #####")
    print("#####      4 - Módulo Relatório        #####")
    print("#####      5 - Módulo Informações      #####")
    print("#####      0 - Sair                    #####")
    resp = input("##### Escolha sua opção: ")
    print()

    if resp == '1':
        resp2 = ''
        while resp2 != '0':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("############################################")
            print("######       Módulo Cliente       ######")
            print("############################################")
            print()
            print("#####      1 - Cadastrar Cliente            #####")
            print("#####      2 - Pesquisar Cliente        #####")
            print("#####      3 - Atualizar Cadastro            #####")
            print("#####      4 - Deletar Cadastro        #####")
            print("#####      0 - Sair                    #####")
            resp2 = input("##### Escolha sua opção: ")
            print()

            if resp2 == '1':
                os.system('cls' if os.name == 'nt' else 'clear')

                print("############################################")
                print("######       Cadastrar Cliente       ######")
                print("############################################")
                print()
                nome = input("##### Digite o nome da empresa: ")
                print()
                razao = input("##### Digite a razão social da empresa: ")
                print()
                cnpj = input("##### Digite o CNPJ da empresa: ")
                print()
                telefone = input("##### Digite o telefone de contato da empresa: ")
                print()
                local = input("##### Digite a localização da empresa (UF incluso): ")
                print()
                clientes[nome] = [razao, cnpj, telefone, local]
                print("Clientes: ", clientes)
                print()
                print("#### Cliente cadastrado com sucesso!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '2':
                os.system('cls' if os.name == 'nt' else 'clear')

                print("############################################")
                print("######       Pesquisar Cliente       ######")
                print("############################################")
                print()
                nome = input("##### Digite o nome da empresa: ")
                print()
                if nome in clientes:
                    print("##### Razão Social: ", clientes[nome][0])
                    print("##### CNPJ: ", clientes[nome][1])
                    print("##### Telefone: ", clientes[nome][2])
                    print("##### Localização: ", clientes[nome][3])
                else:
                    print(nome, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '3':
                os.system('cls' if os.name == 'nt' else 'clear')

                print("############################################")
                print("######       Atualizar Cadastro       ######")
                print("############################################")
                print()
                nome = input("##### Digite o nome da empresa: ")
                print()
                if nome in clientes:
                    print("##### 1 - Razão Social: ", clientes[nome][0])
                    print("##### 2 - CNPJ: ", clientes[nome][1])
                    print("##### 3 - Telefone: ", clientes[nome][2])
                    print("##### 4 - Localização: ", clientes[nome][3])
                    info = input("##### Qual informação deseja alterar? (1,2,3,4)")
                    if info == '1':
                        razao = input("##### Digite a nova razão social: ")
                        clientes[nome][0] = razao
                    elif info == '2':
                        cnpj = input("##### Digite o novo CNPJ: ")
                        clientes[nome][1] = cnpj
                    elif info == '3':
                        telefone = input("##### Digite o novo telefone: ")
                        clientes[nome][2] = telefone
                    elif info == '4':
                        local = input("##### Digite a nova localização: ")
                        clientes[nome][3] = local
                    else:
                        print("##### Opção inválida!")
                else:
                    print(nome, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '4':
                os.system('cls' if os.name == 'nt' else 'clear')

                print("############################################")
                print("######       Deletar Cadastro       ######")
                print("############################################")
                print()
                nome = input("##### Digite o nome da empresa: ")
                print()
                if nome in clientes:
                    print("##### Razão Social: ", clientes[nome][0])
                    print("##### CNPJ: ", clientes[nome][1])
                    print("##### Telefone: ", clientes[nome][2])
                    print("##### Localização: ", clientes[nome][3])
                    certeza = input("##### Você tem certeza que deseja deletar esse cadastro? (s/n) ")
                    if certeza.lower() == 's':
                        del clientes[nome]
                        print("##### Cadastro deletado com sucesso!")
                        print()
                        print("Clientes: ", clientes)
                    else:
                        print("##### Operação cancelada!")
                else:
                    print(nome, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

    elif resp == '2':
        resp2 = ''
        while resp2 != '0':
            os.system('cls' if os.name == 'nt' else 'clear')

            print("############################################")
            print("######       Módulo Produto       ######")
            print("############################################")
            print()
            print("#####      1 - Cadastrar Produto            #####")
            print("#####      2 - Pesquisar Produto        #####")
            print("#####      3 - Atualizar Produto            #####")
            print("#####      4 - Deletar Produto        #####")
            print("#####      0 - Sair                    #####")
            resp2 = input("##### Escolha sua opção: ")
            print()

            if resp2 == '1':
                os.system('cls' if os.name == 'nt' else 'clear')

                print("############################################")
                print("######       Cadastrar Produto       ######")
                print("############################################")
                print()
                nome_produto = input("##### Digite o nome do produto a ser cadastrado: ")
                print()
                descricao_produto = input("##### Dê uma breve descrição do produto: ")
                print()
                preco_produto = float(input("##### Digite o preço (por unidade) do produto: "))
                print()
                quantidade_produto = int(input("##### Digite a qauntidade de unidades do produto em estoque: "))
                print()
                tipo_produto = input("##### Indique a natureza do tipo do produto (chapéu, boné): ")
                print()
                produtos[nome_produto] = [descricao_produto, preco_produto, quantidade_produto, tipo_produto]
                print("Produtos: ", produtos)
                print()
                print("#### Produto cadastrado com sucesso!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '2':
                os.system('cls' if os.name == 'nt' else 'clear')

                print("############################################")
                print("######       Pesquisar Produto       ######")
                print("############################################")
                print()
                nome_produto = input("##### Digite o nome do produto: ")
                if nome_produto in produtos:
                    print("##### Descrição: ", produtos[nome_produto][0])
                    print("##### Preço: ", produtos[nome_produto][1])
                    print("##### Quantidade em estoque: ", produtos[nome_produto][2])
                    print("##### Tipo de produto: ", produtos[nome_produto][3])
                else:
                    print(nome_produto, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '3':
                os.system('cls' if os.name == 'nt' else 'clear')

                print("############################################")
                print("######       Atualizar Produto       ######")
                print("############################################")
                print()
                nome_produto = input("##### Digite o nome do produto: ")
                if nome_produto in produtos:
                    print("##### 1 - Descrição: ", produtos[nome_produto][0])
                    print("##### 2 - Preço: ", produtos[nome_produto][1])
                    print("##### 3 - Quantidade em estoque: ", produtos[nome_produto][2])
                    print("##### 4 - Tipo de produto: ", produtos[nome_produto][3])
                    info = input("##### Qual informação deseja alterar? (1,2,3,4)")
                    if info == '1':
                        descricao_produto = input("##### Digite a nova descrição do produto: ")
                        produtos[nome_produto][0] = descricao_produto
                    elif info == '2':
                        preco_produto = float(input("##### Digite o novo preço do produto: "))
                        produtos[nome_produto][1] = preco_produto
                    elif info == '3':
                        quantidade_produto = int(input("##### Digite a quantidade atualizada de unidades do produto em estoque: "))
                        produtos[nome_produto][2] = quantidade_produto
                    elif info == '4':
                        tipo_produto = input("##### Digite o novo tipo do produto: ")
                        produtos[nome_produto][3] = tipo_produto
                    else:
                        print("##### Opção inválida!")
                else:
                    print(nome_produto, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '4':
                os.system('cls' if os.name == 'nt' else 'clear')

                print("############################################")
                print("######       Deletar Produto       ######")
                print("############################################")
                print()
                nome_produto = input("##### Digite o nome do produto: ")
                if nome_produto in produtos:
                    print("##### Descrição: ", produtos[nome_produto][0])
                    print("##### Preço: ", produtos[nome_produto][1])
                    print("##### Quantidade em estoque: ", produtos[nome_produto][2])
                    print("##### Tipo de produto: ", produtos[nome_produto][3])
                    certeza = input("##### Você tem certeza que deseja deletar esse cadastro de produto? (s/n) ")
                    if certeza.lower() == 's':
                        del produtos[nome_produto]
                        print("##### Cadastro deletado com sucesso!")
                    else:
                        print("##### Operação cancelada!")
                else:
                    print(nome_produto, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

    elif resp == '3':
      resp2 = ''
      while resp2 != '0':
        os.system('cls' if os.name == 'nt' else 'clear')

        print("############################################")
        print("######       Módulo Pedidos       ######")
        print("############################################")
        print()
        print("#####      1 - Cadastrar Pedido            #####")
        print("#####      2 - Pesquisar Pedido        #####")
        print("#####      3 - Atualizar Pedido            #####")
        print("#####      4 - Deletar Pedido        #####")
        print("#####      0 - Sair                    #####")
        resp2 = input("##### Escolha sua opção: ")
        print()

        if resp2 == '1':
          os.system('cls' if os.name == 'nt' else 'clear')

          print("############################################")
          print("#####       Cadastrar Pedido       ####")
          print("############################################")
          print()
          emp_pedido = input("##### Digite a razão social da empresa que fez o pedido: ")
          print()
          prod_pedido = input("##### Digite o nome do produto: ")
          print()
          quant_pedido = int(input("##### Digite a quantidade de unidades do produto desejado: "))
          print()
          data_pedido = datetime.date.today()
          print()
          num_pedido = len(pedidos) + 1
          print("##### Número do pedido: ", num_pedido)
          pedidos[num_pedido] = [emp_pedido, prod_pedido, quant_pedido, data_pedido]
          print()
          print("Pedidos: ", pedidos)
          print()
          print("#### Pedido cadastrado com sucesso!")
          print()
          input("#### Pressione ENTER para continuar.")

        elif resp2 == '2':
          os.system('cls' if os.name == 'nt' else 'clear')

          print("############################################")
          print("#####       Pesquisar Pedido       ####")
          print("############################################")
          print()
          num_pedido = int(input("##### Digite o número do pedido: "))
          print()
          for num_pedido in pedidos:
            print("##### Empresa que fez o pedido: ", pedidos[num_pedido][0])
            print("##### Produto: ", pedidos[num_pedido][1])
            print("##### Quantidade: ", pedidos[num_pedido][2])
            print("##### Data do pedido: ", pedidos[num_pedido][3])
          else:
            print(num_pedido, "não está cadastrado!")
          print()
          input("#### Pressione ENTER para continuar.")

        elif resp2 == '3':
          os.system('cls' if os.name == 'nt' else 'clear')

          print("############################################")
          print("#####       Atualizar Pedido       ####")
          print("############################################")
          print()
          num_pedido = int(input("##### Digite o número do pedido: "))
          print()
          for num_pedido in pedidos:
            print("##### 1 - Empresa que fez o pedido: ", pedidos[num_pedido][0])
            print("##### 2 - Produto: ", pedidos[num_pedido][1])
            print("##### 3 - Quantidade: ", pedidos[num_pedido][2])
            print("##### 4 - Data do pedido: ", pedidos[num_pedido][3])
            info = input("##### Qual informação deseja alterar? (1,2,3,4)")
            if info == '1':
              emp_pedido = input("##### Digite a nova razão social da empresa que fez o pedido: ")
              pedidos[num_pedido][0] = emp_pedido
            elif info == '2':
              prod_pedido = input("##### Digite o novo nome do produto: ")
              pedidos[num_pedido][1] = prod_pedido
            elif info == '3':
              quant_pedido = int(input("##### Digite a nova quantidade de unidades do produto desejado: "))
              pedidos[num_pedido][2] = quant_pedido
            elif info == '4':
              data_pedido = input("##### Digite a nova data do pedido (dd/mm/aaaa): ")
              pedidos[num_pedido][3] = data_pedido
            else:
              print("##### Opção inválida!")
          else:
            print(num_pedido, "não está cadastrado!")
          print()
          input("#### Pressione ENTER para continuar.")

        elif resp2 == '4':
          os.system('cls' if os.name == 'nt' else 'clear')

          print("############################################")
          print("#####       Deletar Pedido       ####")
          print("############################################")
          print()
          num_pedido = int(input("##### Digite o número do pedido: "))
          print()
          for num_pedido in pedidos:
            print("##### Empresa que fez o pedido: ", pedidos[num_pedido][0])
            print("##### Produto: ", pedidos[num_pedido][1])
            print("##### Quantidade: ", pedidos[num_pedido][2])
            print("##### Data do pedido: ", pedidos[num_pedido][3])
            print()
            certeza = input("##### Você tem certeza que deseja deletar esse pedido? (s/n) ")
            if certeza.lower() == 's':
              del pedidos[num_pedido]
              print("##### Pedido deletado com sucesso!")
            else:
              print("##### Operação cancelada!")
          else:
            print(num_pedido, "não está cadastrado!")
          print()
          input("#### Pressione ENTER para continuar.")

    elif resp == '4':
      resp2 == ''
      while resp2 != '0':
        os.system('cls' if os.name == 'nt' else 'clear')

        print("############################################")
        print("#####       Módulo Relatório       ####")
        print("############################################")
        print()
        print("#####      1 - Relatório de Clientes cadastrados           #####")
        print("#####      2 - Relatório de Produtos em estoque        #####")
        print("#####      3 - Relatório de Pedidos cadastrados        #####")
        print("#####      0 - Sair                    #####")
        resp = input("##### Escolha sua opção: ")
        print()
        input("#### Pressione ENTER para continuar.")

    elif resp == '5':
      resp2 == ''
      while resp2 != '0':
        os.system('cls' if os.name == 'nt' else 'clear')

        print("############################################")
        print("#####  Informações sobre nós! ####")
        print("############################################")
        print()
        print("#####  Sistema de gerenciamento e controle de fábrica de chapéus e bonés  ####")
        print("#####  Equipe de desenvolvimento:       ####")
        print("#####  * Marcos Paulo   ####")
        print()
        input("#### Pressione ENTER para continuar.")

    elif resp == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Fim do programa!")

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida!")
        input("#### Pressione ENTER para continuar.")

print("Obrigado por preferir Gentildonnas Attelier!")


arq_pedidos = open("pedidos.dat", "wb")
pickle.dump(pedidos, arq_pedidos)
arq_pedidos.close()


arq_clientes = open("clientes.dat", "wb")
pickle.dump(clientes, arq_clientes)
arq_clientes.close()


arq_produtos = open("produtos.dat", "wb")
pickle.dump(produtos, arq_produtos)
arq_produtos.close()
