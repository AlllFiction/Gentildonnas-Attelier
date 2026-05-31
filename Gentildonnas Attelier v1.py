import os

pedidos = {
    # número do pedido : [[quantidade], [produto], cliente, data]
}

clientes = {
    # nome da empresa : [razão social, cnpj, telefone de contato, localização com UF]
}

produtos = {
    # nome do produto : [código de identificação, preço]
}

resp = ''
while resp != '0':
    os.system('clear')

    print("############################################")
    print("######       Gentildonna's Attelier       ######")
    print("############################################")
    print("#####      1 - Módulo Cliente            #####")
    print("#####      2 - Módulo Produto        #####")
    print("#####      3 - Módulo Pedido            #####")
    print("#####      4 - Módulo Relatório        #####")
    print("#####      5 - Módulo Informações      #####")
    print("#####      0 - Sair                    #####")
    resp = input("##### Escolha sua opção: ")
    print()

    if resp == '1':
     os.system('clear')

     print("############################################")
     print("######       Módulo Cliente       ######")
     print("############################################")
     print("#####      1 - Cadastrar Cliente            #####")
     print("#####      2 - Pesquisar Cliente        #####")
     print("#####      3 - Atualizar Cadastro            #####")
     print("#####      4 - Deletar Cadastro        #####")
     print("#####      5 - Listar Clientes      #####")
     print("#####      0 - Sair                    #####")
     resp2 = input("##### Escolha sua opção: ")
     print()

    if resp2 =='1':
      os.system('clear')

      print("############################################")
      print("######       Cadastrar Cliente       ######")
      print("############################################")
      nome = input("##### Digite o nome da empresa: ")
      razao = input("##### Digite a razão social da empresa: ")
      cnpj = input("##### Digite o CNPJ da empresa: ")
      telefone = input("##### Digite o telefone de contato da empresa: ")
      local = input("##### Digite a localização da empresa (UF incluso): ")
      clientes[nome] = [razao, cnpj, telefone, local]
      print()

    elif resp2 == '2':
      os.system('clear')

      print("############################################")
      print("######       Pesquisar Cliente       ######")
      print("############################################")
      nome = input("##### Digite o nome da empresa: ")
      if nome in clientes:
        print("##### Razão Social: ", clientes[nome][0])
        print("##### CNPJ: ", clientes[nome][1])
        print("##### Telefone: ", clientes[nome][2])
        print("##### Localização: ", clientes[nome][3])
      else:
        print(nome, "não está cadastrado!")
      print()

    elif resp2 == '3':
      os.system('clear')

      print("############################################")
      print("######       Atualizar Cadastro       ######")
      print("############################################")
      nome = input("##### Digite o nome da empresa: ")
      if nome in clientes:
        print("##### 1 - Razão Social: ", clientes[nome][0])
        print("##### 2 - CNPJ: ", clientes[nome][1])
        print("##### 3 - Telefone: ", clientes[nome][2])
        print("##### 4 - Localização: ", clientes[nome][3])
        info = input("##### Qual informação deseja alterar? ")
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

    elif resp2 == '4':
      os.system('clear')

      print("############################################")
      print("######       Deletar Cadastro       ######")
      print("############################################")
      nome = input("##### Digite o nome da empresa: ")
      if nome in clientes:
        print("##### Razão Social: ", clientes[nome][0])
        print("##### CNPJ: ", clientes[nome][1])
        print("##### Telefone: ", clientes[nome][2])
        print("##### Localização: ", clientes[nome][3])
        certeza = input("##### Você tem certeza que deseja deletar esse cadastro? (s/n) ")
        if certeza == 's':
          del clientes[nome]
          print("##### Cadastro deletado com sucesso!")
        else:
          print("##### Operação cancelada!")
      else:
        print(nome, "não está cadastrado!")
      print()

    elif resp2 == '5':
      os.system('clear')

      print("############################################")
      print("######       Listar Clientes       ######")
      print("############################################")
      for nome in clientes:
        print("##### Clientes cadastrados: ", clientes[nome][0])
        print()

    elif resp == '2':
      os.system('clear')
      print("############################################")
      print("#####               ATENÇÃO                    ####")
      print("#####      Este módulo ainda está       ####")
      print("#####        em desenvolvimento!!         ####")
      print("#####                                   ####")
      print("############################################")
      print()

    elif resp == '3':
      os.system('clear')

      print("############################################")
      print("#####               ATENÇÃO                    ####")
      print("#####      Este módulo ainda está       ####")
      print("#####        em desenvolvimento!!         ####")
      print("#####                                   ####")
      print("############################################")
      print()

    elif resp == '4':
      os.system('clear')

      print("############################################")
      print("#####               ATENÇÃO                    ####")
      print("#####      Este módulo ainda está       ####")
      print("#####        em desenvolvimento!!         ####")
      print("#####                                   ####")
      print("############################################")
      print()

    elif resp == '5':
      os.system('clear')

      print("############################################")
      print("#####  Informações sobre nós! ####")
      print("############################################")
      print()
      print("#####  Sistema de gerenciamento e controle de fábrica de chapéus e bonés  ####")
      print("#####  Equipe de desenvolvimento:       ####")
      print("#####  * Marcos Paulo Florêncio da Silva  ####")
      print()

    elif resp == '0':
      os.system('clear')

      print("Fim do programa!")
      print("Obrigado pela preferência!")

    else:
      os.system('clear')
      print("Opção inválida!")
