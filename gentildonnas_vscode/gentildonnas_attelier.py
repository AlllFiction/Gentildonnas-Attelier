import os
import datetime
import fun_clientes
import fun_produtos
import fun_pedidos

clientes = fun_clientes.recupera_clientes()
produtos = fun_produtos.recupera_produtos()
pedidos = fun_pedidos.recupera_pedidos()


# clientes = {
    # cnpj da empresa : [razão social, telefone de contato, localização, UF, status]
# }


# produtos = {
    # código de identificação : [nome, preço, categoria, quantidade em estoque, status]
# }


# pedidos = {
    # número do pedido : [cliente, produto, quantidade, data, status]
# }


resp = ''
while resp != '0':
    os.system('cls' if os.name == 'nt' else 'clear')

    print('''
          ############################################
          #######    Gentildonna's Attelier    #######
          ############################################

          ######      1 - Módulo Cliente          #####
          ######      2 - Módulo Produto          #####
          ######      3 - Módulo Pedido           #####
          ######      4 - Módulo Relatório        #####
          ######      5 - Módulo Informações      #####
          ######      0 - Sair                    #####

    ''')
    resp = input("##### Escolha sua opção: ")
    print()

    if resp == '1':
        resp2 = ''
        while resp2 != '0':
            os.system('cls' if os.name == 'nt' else 'clear')

            print('''
                  ############################################
                  #######         Módulo Cliente        ######
                  ############################################

                  ######      1 - Cadastrar Cliente        #####
                  ######      2 - Pesquisar Cliente        #####
                  ######      3 - Atualizar Cadastro       #####
                  ######      4 - Desativar Cadastro       #####
                  ######      0 - Sair                     #####
            
            ''')
            resp2 = input("##### Escolha sua opção: ")
            print()

            if resp2 == '1':
                os.system('cls' if os.name == 'nt' else 'clear')

                print('''
                      ############################################
                      ######        Cadastrar Cliente       ######
                      ############################################
                      
                ''')

                certeza = ''
                while certeza != 's':

                    cnpj = input("##### Informe os digitos do CNPJ da empresa: ")
                    while fun_clientes.confirma_cnpj(cnpj) == False:
                        print("Ops! Houve algum erro...")
                        print("Tente novamente!")
                        cnpj = input("##### Informe os digitos do CNPJ da empresa: ")
                        print()

                    razao = input("##### Informe a razão social da empresa: ")
                    print()

                    telefone = input("##### Informe o telefone de contato da empresa (com o DDD): ")
                    while fun_clientes.confirma_tel(telefone) == False:
                       print("Ops! Houve algum erro...")
                       print("tente novamente!")
                       telefone = input("##### Informe o telefone de contato da empresa (com o DDD): ")
                    print()

                    local = input("##### Informe a localização da empresa: ")
                    while fun_clientes.confirma_local(local) == False:
                        print("Ops! Houve algum erro...")
                        print("Tente novamente!")
                        local = input("##### Informe a localização da empresa: ")
                    print()

                    uf = input("##### Informe o UF da localização: ").upper()
                    while fun_clientes.confirma_uf(uf) == False:
                        print("Ops! Houve algum erro...")
                        print("Tente novamente!")
                        uf = input("##### Informe o UF da localização: ")
                    print()

                    status_cli = True
                    print()

                    print("Dados: ", cnpj, razao, telefone, local, uf, status_cli)
                    print()
                    certeza = input("Tem certeza que os dados estão corretos? (s/n)").lower()
                clientes[cnpj] = [razao, telefone, local, uf, status_cli]
                print()
                print("#### Cliente cadastrado com sucesso!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '2':
                os.system('cls' if os.name == 'nt' else 'clear')

                print('''
                      ############################################
                      #######       Pesquisar Cliente       ######
                      ############################################
                      
                ''')

                cnpj = input("##### Digite o CNPJ da empresa: ")
                print()
                if cnpj in clientes:
                    if clientes[cnpj][4] == True:
                        print("##### Razão Social: \t", clientes[cnpj][0])
                        print("##### Telefone: \t", clientes[cnpj][1])
                        print("##### Localização: \t", clientes[cnpj][2], "-", clientes[cnpj][3])
                    else:
                       print(cnpj, "inativo!")
                else:
                    print(cnpj, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '3':
                os.system('cls' if os.name == 'nt' else 'clear')

                print('''
                      #############################################
                      ######       Atualizar Cadastro        ######
                      #############################################

                ''')

                cnpj = input("##### Digite o CNPJ da empresa: ")
                print()
                if cnpj in clientes:
                    if clientes[cnpj][4] == True:
                        print("##### 1 - Razão Social: \t", clientes[cnpj][0])
                        print("##### 2 - Telefone: \t", clientes[cnpj][1])
                        print("##### 3 - Localização: \t", clientes[cnpj][2])
                        print("##### 4 - UF: \t", clientes[cnpj][3])
                        info = input("##### Qual informação deseja alterar? (1,2,3,4)")
                        if info == '1':
                            razao = input("##### Informe a nova Razão Social: ")
                            clientes[cnpj][0] = razao
                        elif info == '2':
                            telefone = input("##### Informe o novo telefone: ")
                        elif info == '3':
                            telefone = input("##### Informe a nova Localização: ")
                            clientes[cnpj][2] = local
                        elif info == '4':
                            uf = input("##### Informe a nova UF: ")
                            clientes[cnpj][3] = uf
                        else:
                            print("##### Opção inválida!")
                    else:
                       print(cnpj, "inativo!")
                else:
                    print(cnpj, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '4':
                os.system('cls' if os.name == 'nt' else 'clear')

                print('''
                      ##############################################
                      #######       Desativar Cadastro        ######
                      ##############################################
                ''')

                cnpj = input("##### Digite o CNPJ da empresa: ")
                print()
                if cnpj in clientes:
                    if clientes[cnpj][4] == True:
                        print("##### Razão Social: \t", clientes[cnpj][0])
                        print("##### Telefone: \t", clientes[cnpj][1])
                        print("##### Localização: \t", clientes[cnpj][2], "-", clientes[cnpj][3])
                        certeza = input("##### Você tem certeza que deseja cancelar esse cadastro? (s/n) ")
                        if certeza.lower() == 's':
                            clientes[cnpj][4] = False
                            print("##### Cadastro desativado com sucesso!")
                        else:
                            print("##### Operação cancelada!")
                    else:
                       print(cnpj, "inativo!")
                else:
                    print(cnpj, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

    elif resp == '2':
        resp2 = ''
        while resp2 != '0':
            os.system('cls' if os.name == 'nt' else 'clear')

            print('''
                  ############################################
                  #######       Módulo Produto        ########
                  ############################################

                  ######      1 - Cadastrar Produto        #####
                  ######      2 - Pesquisar Produto        #####
                  ######      3 - Atualizar Produto        #####
                  ######      4 - Desativar Produto        #####
                  ######      0 - Sair                     #####
                  
            ''')

            resp2 = input("##### Escolha sua opção: ")
            print()

            if resp2 == '1':
                os.system('cls' if os.name == 'nt' else 'clear')

                print('''
                      #############################################
                      #######       Cadastrar Produto        ######
                      #############################################
                      
                ''')

                nome_pro = input("##### Informe o nome do produto a ser cadastrado: ")
                print()
                preco = float(input("##### Digite o preço (por unidade) do produto: "))
                print()
                categoria = input("#### Informe a categoria do produto com 1 (chapéu) ou 2 (boné): ")
                if categoria == '1':
                   categoria = "chapeu"
                elif categoria == '2':
                   categoria = 'bone'
                while categoria != '1' or '2':
                   print("Ops! Houve algum erro...")
                   print("Tente novamente!")
                   categoria = input("#### Informe a categoria do produto com 1 (chapéu) ou 2 (boné): ")
                print()
                quantidade = int(input("##### Digite a quantidade de unidades do produto em estoque: "))
                print()
                status_pro = True
                print()
                cod_pro = str(len(produtos) + 1)
                print("O Código do Produto é:", cod_pro)
                produtos[cod_pro] = [nome_pro, preco, categoria, quantidade, status_pro]
                print("#### Produto cadastrado com sucesso!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '2':
                os.system('cls' if os.name == 'nt' else 'clear')

                print('''
                      #############################################
                      #######       Pesquisar Produto        ######
                      #############################################
                ''')

                cod_pro = input("##### Informe o código do produto que procura: ")
                print()
                if cod_pro in produtos:
                    if produtos[cod_pro][4] == True:
                        print('''
                              ###########################################
                              #######        Ficha Produto        #######
                              ###########################################

                        ''')

                        print("##### Nome: \t", produtos[cod_pro][0])
                        print("##### Preço: \t R$ %.2f" %(produtos[cod_pro][1]))
                        print("#### Categoria: \t", produtos[cod_pro][2])
                        print("##### Quantidade em estoque: \t", produtos[cod_pro][3])
                    else:
                       print(cod_pro, "inativo!")
                else:
                    print(cod_pro, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '3':
                os.system('cls' if os.name == 'nt' else 'clear')

                print('''
                      ##############################################
                      #######        Atualizar Produto        ######
                      ##############################################
                      
                ''')

                cod_pro = input("##### Digite o nome do produto: ")
                if cod_pro in produtos:
                    if produtos[cod_pro][4] == True:
                        print("##### 1 - Nome: ", produtos[cod_pro][0])
                        print("##### 2 - Preço: ", produtos[cod_pro][1])
                        print("##### 3 - Categoria: ", produtos[cod_pro][2])
                        print("##### 4 - Quantidade em estoque: ", produtos[cod_pro][3])
                        print()
                        info = input("##### Qual informação deseja alterar? (1,2,3,4)")
                        print()
                        if info == '1':
                            nome_pro = input("##### Digite a nova descrição do produto: ")
                            produtos[cod_pro][0] = nome_pro
                        elif info == '2':
                            preco = float(input("##### Digite o novo preço do produto: "))
                            produtos[cod_pro][1] = preco
                        elif info == '3':
                            categoria = int(input("##### Digite a quantidade atualizada de unidades do produto em estoque: "))
                            produtos[cod_pro][2] = categoria
                        elif info == '4':
                            estoque = input("##### Digite a quantidade atualizada de unidades do produto em estoque: ")
                            produtos[cod_pro][3] = estoque
                        else:
                            print("##### Opção inválida!")
                    else:
                       print(cod_pro, "inativo!")
                else:
                    print(cod_pro, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

            elif resp2 == '4':
                os.system('cls' if os.name == 'nt' else 'clear')

                print('''
                      ##############################################
                      #######       Desativar Produto        #######
                      ##############################################

                ''')

                cod_pro = input("##### Digite o código do produto: ")
                if cod_pro in produtos:
                    if produtos[cod_pro][4] == True:
                        print("##### Descrição: ", produtos[cod_pro][0])
                        print("##### Preço: ", produtos[cod_pro][1])
                        print("##### Quantidade em estoque: ", produtos[cod_pro][2])
                        print("##### Tipo de produto: ", produtos[cod_pro][3])
                        certeza = input("##### Você tem certeza que deseja deletar esse cadastro de produto? (s/n) ")
                        if certeza.lower() == 's':
                            produtos[cod_pro][4]
                            print("##### Cadastro deletado com sucesso!")
                        else:
                            print("##### Operação cancelada!")
                    else:
                       print(cod_pro, "inativo!")
                else:
                    print(cod_pro, "não está cadastrado!")
                print()
                input("#### Pressione ENTER para continuar.")

    elif resp == '3':
      resp2 = ''
      while resp2 != '0':
        os.system('cls' if os.name == 'nt' else 'clear')

        print('''
              ############################################
              #######        Módulo Pedidos        #######
              ############################################

              ######      1 - Cadastrar Pedido        #####
              ######      2 - Pesquisar Pedido        #####
              ######      3 - Atualizar Pedido        #####
              ######      4 - Cancelar Pedido         #####
              ######      0 - Sair                    #####
              
        ''')

        resp2 = input("##### Escolha sua opção: ")
        print()

        if resp2 == '1':
          os.system('cls' if os.name == 'nt' else 'clear')

          print('''
                ############################################
                ######        Cadastrar Pedido        ######
                ############################################

            ''')
          
          cnpj = input("##### Digite o CNPJ da empresa que fez o pedido: ")
          if cnpj in clientes:
             if clientes[cnpj][4] == True:
                print("#### Empresa selecionada:", clientes[cnpj][0])
          else:
             print(cnpj, "não está cadastrado!")
          print()

          cod_pro = input("##### Digite o código de identificação do produto desejado: ")
          if cod_pro in produtos:
             if produtos[cod_pro][4] == True:
                print("#### Produto selecionado:", produtos[cod_pro][0])
          else:
             print(cod_pro, "não está cadastrado!")
          print()

          quant_pedido = int(input("##### Digite a quantidade de unidades do produto desejado: "))          
          print()
          dia = datetime.date.today()
          data_pedido = dia.strftime("%d/%m/%y")
          print()
          status_pe = True
          num_pedido = str(len(pedidos) + 1)
          print("##### Número do pedido: ", num_pedido)
          pedidos[num_pedido] = [cnpj, cod_pro, quant_pedido, data_pedido, status_pe]
          print()
          print("#### Pedido cadastrado com sucesso!")
          print()
          input("#### Pressione ENTER para continuar.")

        elif resp2 == '2':
          os.system('cls' if os.name == 'nt' else 'clear')

          print('''
                ############################################
                ######        Pesquisar Pedido        ######
                ############################################

          ''')

          num_pedido = (input("##### Digite o número do pedido: "))
          print()
          if num_pedido in pedidos:
            if pedidos[num_pedido][4] == True:
                print("##### Empresa que fez o pedido: ", pedidos[num_pedido][0])
                print("##### Produto: ", pedidos[num_pedido][1])
                print("##### Quantidade: ", pedidos[num_pedido][2])
                print("##### Data do pedido: ", pedidos[num_pedido][3])
            else:
               print(num_pedido, "inativo!")
          else:
            print(num_pedido, "não está cadastrado!")
          print()
          input("#### Pressione ENTER para continuar.")

        elif resp2 == '3':
          os.system('cls' if os.name == 'nt' else 'clear')

          print('''
                ############################################
                ######        Atualizar Pedido        ######
                ############################################

          ''')

          num_pedido = (input("##### Digite o número do pedido: "))
          print()
          if num_pedido in pedidos:
            if pedidos[num_pedido][4] == True:
                print("##### 1 - Empresa que fez o pedido: ", pedidos[num_pedido][0])
                print("##### 2 - Produto: ", pedidos[num_pedido][1])
                print("##### 3 - Quantidade: ", pedidos[num_pedido][2])
                info = input("##### Qual informação deseja alterar? (1,2,3)")
                if info == '1':
                   emp_pedido = input("##### Digite o CNPJ da empresa que fez o pedido: ")
                   pedidos[num_pedido][0] = emp_pedido
                   print("Atualização concluida com sucesso!")
                elif info == '2':
                   prod_pedido = input("##### Digite o nome do produto: ")
                   pedidos[num_pedido][1] = prod_pedido
                   print("Atualização concluida com sucesso!")
                elif info == '3':
                   quant_pedido = int(input("##### Digite a nova quantidade de unidades do produto desejado: "))
                   pedidos[num_pedido][2] = quant_pedido
                   print("Atualização concluida com sucesso!")
                else:
                   print("##### Opção inválida!")
            else:
               print(num_pedido, "inativo!")
          else:
            print(num_pedido, "não está cadastrado!")
          print()
          input("#### Pressione ENTER para continuar.")

        elif resp2 == '4':
          os.system('cls' if os.name == 'nt' else 'clear')

          print('''
                ############################################
                ######        Cancelar Pedido        #######
                ############################################
          ''')

          num_pedido = (input("##### Digite o número do pedido: "))
          print()
          if num_pedido in pedidos:
            if pedidos[num_pedido][4] == True:
                print("##### Empresa que fez o pedido: ", pedidos[num_pedido][0])
                print("##### Produto: ", pedidos[num_pedido][1])
                print("##### Quantidade: ", pedidos[num_pedido][2])
                print("##### Data do pedido: ", pedidos[num_pedido][3])
                print()
                certeza = input("##### Você tem certeza que deseja deletar esse pedido? (s/n) ")
                if certeza.lower() == 's':
                   pedidos[num_pedido][4] == False
                   print("##### Pedido Cancelado com sucesso!")
                else:
                   print("##### Operação cancelada!")
            else:
               print(num_pedido, "inativo!")
          else:
            print(num_pedido, "não está cadastrado!")
          print()
          input("#### Pressione ENTER para continuar.")

    elif resp == '4':
      resp2 = ''
      while resp2 != '0':
        os.system('cls' if os.name == 'nt' else 'clear')

        print('''
              ############################################
              ######        Módulo Relatório        ######
              ############################################

              ######      1 - Relatórios de Clientes       #####
              ######      2 - Relatórios de Produtos       #####
              ######      3 - Relatórios de Pedidos        #####
              ######      0 - Sair                         #####

        ''')

        resp2 = input("##### Escolha sua opção: ")
        print()

        if resp2 == '1':
           resp3 = ''
           while resp3 != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print('''
                    ################################################
                    ######       Relatórios de Clientes       ######
                    ################################################

                    ######      1 - Relatório Geral de Clientes         #####
                    ######      2 - Relatório por dados                 #####
                    ######      0 - Sair                                #####

            ''')

            resp3 = input("##### Escolha sua opção: ")
            print()

            if resp3 == '1':
               os.system('cls' if os.name == 'nt' else 'clear')
               
               print()
               print("############################################")
               print("######    Relatório Geral de Clientes   ####")
               print("############################################")
               print()
               for cnpj, dados in clientes.items():
                  print("CNPJ do cliente: ", cnpj)
                  print("Razão Social do cliente: ", dados[0])
                  print("Telefone do cliente: ", dados[1])
                  print("Localização do cliente: ", dados[2], "-", dados[3])
                  print("Status do cliente: ", dados[4])
                  print("--------------------------------------")
               print()
               input("#### Pressione ENTER para continuar.")


            elif resp3 == '2':
               resp4 = ''
               while resp4 != '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                print()
                print("###############################################")
                print("######   Relatório de dados de Clientes   #####")
                print("###############################################")
                print()
                print('''
                        #### 1 - Razão Social.
                        #### 2 - Telefone.
                        #### 3 - Localização.
                        #### 4 - UF.
                        #### 5 - Status (ativo ou inativo).
                    ''')
                resp4 = input("#### A partir de qual informação deseja começar sua busca?")

                if resp4 == '1':
                   os.system('cls' if os.name == 'nt' else 'clear')
                   print()
                   print("############################################")
                   print("######       Relatório Razão Social       ####")
                   print("############################################")
                   print()
                   razao_pro = input("#### Insira a Razão Social que procura: ")
                   encontrou = False
                   print()

                   for cnpj, dados in clientes.items():
                      razao = dados[0]

                      if razao.lower().startswith(razao_pro.lower()):
                         print("CNPJ do cliente: ", cnpj)
                         print("Razão Social do cliente: ", dados[0])
                         print("Telefone do cliente: ", dados[1])
                         print("Localização do cliente: ", dados[2], "-", dados[3])
                         print("Status do cliente: ", dados[4])
                         print("--------------------------------------")
                         encontrou = True

                   if encontrou == False:
                    print("Razão Social não encontrada!")

                   print()
                   input("#### Pressione ENTER para continuar.")

                
                if resp4 == '2':
                   os.system('cls' if os.name == 'nt' else 'clear')
                   print()
                   print("############################################")
                   print("######       Relatório Telefone       ####")
                   print("############################################")
                   print()
                   tel_pro = input("#### Insira o número de Telefone que procura: ")
                   encontrou = False
                   print()

                   for cnpj, dados in clientes.items():
                      telefone = dados[1]

                      if telefone.lower().startswith(tel_pro.lower()):
                         print("CNPJ do cliente: ", cnpj)
                         print("Razão Social do cliente: ", dados[0])
                         print("Telefone do cliente: ", dados[1])
                         print("Localização do cliente: ", dados[2], "-", dados[3])
                         print("Status do cliente: ", dados[4])
                         print("--------------------------------------")
                         encontrou = True

                   if encontrou == False:
                    print("número de Telefone não encontrado!")

                   print()
                   input("#### Pressione ENTER para continuar.")


                if resp4 == '3':
                   os.system('cls' if os.name == 'nt' else 'clear')
                   print()
                   print("############################################")
                   print("######       Relatório Localização       ####")
                   print("############################################")
                   print()
                   local_pro = input("#### Insira a Localização que procura: ")
                   encontrou = False
                   print()

                   for cnpj, dados in clientes.items():
                      razao = dados[0]

                      if local.lower().startswith(local_pro.lower()):
                         print("CNPJ do cliente: ", cnpj)
                         print("Razão Social do cliente: ", dados[0])
                         print("Telefone do cliente: ", dados[1])
                         print("Localização do cliente: ", dados[2], "-", dados[3])
                         print("Status do cliente: ", dados[4])
                         print("--------------------------------------")
                         encontrou = True

                   if encontrou == False:
                    print("Localização não encontrada!")

                   print()
                   input("#### Pressione ENTER para continuar.")
                

                if resp4 == '4':
                   os.system('cls' if os.name == 'nt' else 'clear')
                   print()
                   print("############################################")
                   print("######       Relatório UF       ####")
                   print("############################################")
                   print()
                   uf_pro = input("#### Insira a UF que procura: ")
                   encontrou = False
                   print()

                   for cnpj, dados in clientes.items():
                      uf = dados[3]

                      if uf.lower().startswith(uf_pro.lower()):
                         print("CNPJ do cliente: ", cnpj)
                         print("Razão Social do cliente: ", dados[0])
                         print("Telefone do cliente: ", dados[1])
                         print("Localização do cliente: ", dados[2], "-", dados[3])
                         print("Status do cliente: ", dados[4])
                         print("--------------------------------------")
                         encontrou = True

                   if encontrou == False:
                    print("UF não encontrada!")

                   print()
                   input("#### Pressione ENTER para continuar.")


                
                if resp4 == '5':
                   os.system('cls' if os.name == 'nt' else 'clear')
                   print()
                   print("############################################")
                   print("######       Relatório Status       ####")
                   print("############################################")
                   print()
                   status = input("#### Qual opção de status deseja ver? Ativos(1), Inativos(2): ")
                   encontrou = False
                   print()

                   for cnpj, dados in clientes.items():

                      if status == '1':
                         if dados[4] == True:
                            print("CNPJ do cliente: ", cnpj)
                            print("Razão Social do cliente: ", dados[0])
                            print("Telefone do cliente: ", dados[1])
                            print("Localização do cliente: ", dados[2], "-", dados[3])
                            print("Status do cliente: ", dados[4])
                            print("--------------------------------------")
                            encontrou = True

                      elif status == '2':
                        if dados[4] == False:
                            print("CNPJ do cliente: ", cnpj)
                            print("Razão Social do cliente: ", dados[0])
                            print("Telefone do cliente: ", dados[1])
                            print("Localização do cliente: ", dados[2], "-", dados[3])
                            print("Status do cliente: ", dados[4])
                            print("--------------------------------------")
                            encontrou = True

                        else:
                           print("#### Insira um valor válido!")                    

                   if encontrou == False:
                    print("Razão Social não encontrada!")

                   print()
                   input("#### Pressione ENTER para continuar.")


        elif resp2 == '2':
           resp3 = ''
           while resp3 != '0':
              os.system('cls' if os.name == 'nt' else 'clear')

              print('''
                    ################################################
                    ######       Relatórios de Produtos      ######
                    ################################################

                    ######      1 - Relatório Geral de Produtos         #####
                    ######      2 - Relatório por dados                 #####
                    ######      0 - Sair                                #####

               ''')
              resp3 = input("#### Escolha sua opção: ")


              if resp3 == '1':
               os.system('cls' if os.name == 'nt' else 'clear')
               
               print()
               print("############################################")
               print("######    Relatório Geral de Produtos   ####")
               print("############################################")
               print()
               for cod_pro, dados in produtos.items():
                  print("Código de Identificação do produto: ", cod_pro)
                  print("Nome do Produto: ", dados[0])
                  print("Preço do Produto: R$ %.2f " %dados[1])
                  print("Categoria do Produto: ", dados[2])
                  print("Quantidade em Estoque: ", dados[3])
                  print("Status do Produto: ", dados[4])
                  print("--------------------------------------")
               print()
               input("#### Pressione ENTER para continuar.")


              elif resp3 == '2':
                resp4 = ''
                while resp4 != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print()
                    print("###############################################")
                    print("######   Relatório de dados de Produtos   #####")
                    print("###############################################")
                    print()
                    print('''
                            #### 1 - Nome do Produto.
                            #### 2 - Faixa de Preço.
                            #### 3 - Categoria.
                            #### 4 - em Estoque.
                            #### 5 - Status (ativo ou inativo).
                        ''')
                    resp4 = input("#### A partir de qual informação deseja começar sua busca?")


                    if resp4 == '1':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print()
                        print("############################################")
                        print("######       Relatório por Nome       ####")
                        print("############################################")
                        print()
                        nome_bus = input("#### Insira o Nome do produto que procura: ")
                        encontrou = False
                        print()

                        for cod_pro, dados in produtos.items():
                            nome_pro = dados[0]

                            if nome_pro.lower().startswith(nome_bus.lower()):
                                print("Código de Identificação do produto: ", cod_pro)
                                print("Nome do Produto: ", dados[0])
                                print("Preço do Produto: R$ %.2f " %dados[1])
                                print("Categoria do Produto: ", dados[2])
                                print("Quantidade em Estoque: ", dados[3])
                                print("Status do Produto: ", dados[4])
                                print("--------------------------------------")
                                encontrou = True

                        if encontrou == False:
                            print("Produto não encontrado!")

                        print()
                        input("#### Pressione ENTER para continuar.")

                    

                    if resp4 == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print()
                        print("############################################")
                        print("######       Relatório por Faixa de Preço       ####")
                        print("############################################")
                        print()
                        preco_min = float(input("#### Insira o valor mínimo que procura: "))
                        preco_max = float(input("#### Insira o valor máximo que procura: "))
                        encontrou = False
                        print()

                        for cod_pro, dados in produtos.items():
                            preco = dados[1]

                            if preco >= preco_min and preco <= preco_max:
                                print("Código de Identificação do produto: ", cod_pro)
                                print("Nome do Produto: ", dados[0])
                                print("Preço do Produto: R$ %.2f " %dados[1])
                                print("Categoria do Produto: ", dados[2])
                                print("Quantidade em Estoque: ", dados[3])
                                print("Status do Produto: ", dados[4])
                                print("--------------------------------------")
                                encontrou = True

                        if encontrou == False:
                            print("Produto não encontrado!")

                        print()
                        input("#### Pressione ENTER para continuar.")



                    if resp4 == '3':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print()
                        print("############################################")
                        print("######       Relatório por Categoria       ####")
                        print("############################################")
                        print()
                        cate_bus = input("#### Indique a Categoria que procura (chapéu/1), (boné/2): ")
                        encontrou = False
                        print()

                        if cate_bus == '1':
                           cate_pro = 'chapeu'

                           for cod_pro, dados in produtos.items():
                                
                                if dados[2].lower() == cate_pro:
                                    print("Código de Identificação do produto: ", cod_pro)
                                    print("Nome do Produto: ", dados[0])
                                    print("Preço do Produto: R$ %.2f " %dados[1])
                                    print("Categoria do Produto: ", dados[2])
                                    print("Quantidade em Estoque: ", dados[3])
                                    print("Status do Produto: ", dados[4])
                                    print("--------------------------------------")
                                    encontrou = True

                        elif cate_bus == '2':
                            cate_pro = 'bone'

                            for cod_pro, dados in produtos.items():
                               
                               if dados[2].lower == cate_pro:
                                    print("Código de Identificação do produto: ", cod_pro)
                                    print("Nome do Produto: ", dados[0])
                                    print("Preço do Produto: R$ %.2f " %dados[1])
                                    print("Categoria do Produto: ", dados[2])
                                    print("Quantidade em Estoque: ", dados[3])
                                    print("Status do Produto: ", dados[4])
                                    print("--------------------------------------")
                                    encontrou = True

                        else:
                           print("#### Digite um valor válido (1 ou 2)!")

                        if encontrou == False:
                            print("Produto não encontrado!")

                        print()
                        input("#### Pressione ENTER para continuar.")

                
                
                    elif resp4 == '4':
                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("############################################")
                        print("######       Relatório por Estoque       ####")
                        print("############################################")
                        print()
                        estoque_bus = input("#### Deseja ver os produtos em estoque (1) ou os produtos fora de estoque (2): ")
                        encontrou = False
                        print()

                        if estoque_bus == '1':
                            for cod_pro, dados in produtos.items():
                                estoque = dados[3]

                                if estoque > 0:
                                    print("Código de Identificação do produto: ", cod_pro)
                                    print("Nome do Produto: ", dados[0])
                                    print("Preço do Produto: R$ %.2f " %dados[1])
                                    print("Categoria do Produto: ", dados[2])
                                    print("Quantidade em Estoque: ", dados[3])
                                    print("Status do Produto: ", dados[4])
                                    print("--------------------------------------")
                                    encontrou = True

                        elif estoque_bus == '2':
                            for cod_pro, dados in produtos.items():
                                estoque = dados[3]

                                if estoque <= 0:
                                    print("Código de Identificação do produto: ", cod_pro)
                                    print("Nome do Produto: ", dados[0])
                                    print("Preço do Produto: R$ %.2f " %dados[1])
                                    print("Categoria do Produto: ", dados[2])
                                    print("Quantidade em Estoque: ", dados[3])
                                    print("Status do Produto: ", dados[4])
                                    print("--------------------------------------")
                                    encontrou = True

                        else:
                           print("#### Digite um valor válido!")

                        if encontrou == False:
                            print("Produto não encontrado!")

                        print()
                        input("#### Pressione ENTER para continuar.")
                    

                    elif resp4 == '5':
                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("############################################")
                        print("######       Relatório Status       ####")
                        print("############################################")
                        print()
                        status = input("#### Qual opção de status deseja ver? Ativos(1), Inativos(2): ")
                        encontrou = False
                        print()

                        for cod_pro, dados in produtos.items():

                            if status == '1':
                                if dados[4] == True:
                                    print("Código de Identificação do produto: ", cod_pro)
                                    print("Nome do Produto: ", dados[0])
                                    print("Preço do Produto: R$ %.2f " %dados[1])
                                    print("Categoria do Produto: ", dados[2])
                                    print("Quantidade em Estoque: ", dados[3])
                                    print("Status do Produto: ", dados[4])
                                    print("--------------------------------------")
                                    encontrou = True

                            elif status == '2':
                                if dados[4] == False:
                                    print("Código de Identificação do produto: ", cod_pro)
                                    print("Nome do Produto: ", dados[0])
                                    print("Preço do Produto: R$ %.2f " %dados[1])
                                    print("Categoria do Produto: ", dados[2])
                                    print("Quantidade em Estoque: ", dados[3])
                                    print("Status do Produto: ", dados[4])
                                    print("--------------------------------------")
                                    encontrou = True

                            else:
                               print("#### Insira um valor válido!")

                        if encontrou == False:
                            print("Produto não encontrado!")

                        print()
                        input("#### Pressione ENTER para continuar.")

            
        elif resp2 == '3':
           resp3 = ''
           while resp3 != '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print('''
                    ################################################
                    ######       Relatórios de Clientes       ######
                    ################################################

                    ######      1 - Relatório Geral de Pedidos         #####
                    ######      2 - Relatório por dados                 #####
                    ######      2 - Relatório por Período                 #####
                    ######      0 - Sair                                #####

            ''')
            resp3 = input("#### Insira a opção desejada: ")

            
            if resp3 == '1':
               os.system('cls' if os.name == 'nt' else 'clear')
               
               print("############################################")
               print("######    Relatório Geral de Pedidos   ####")
               print("############################################")
               print()
               for num_pedido, dados in pedidos.items():
                  print("ID do Pedido: ", num_pedido)
                  print("CNPJ do cliente: ", dados[0])
                  print("ID do Produto pedido", dados[1])
                  print("Quantidade pedida: ", dados[2])
                  print("Data do Pedido: ", dados[3])
                  print("Status do Pedido: ", dados[4])
                  print("--------------------------------------")
               print()
               input("#### Pressione ENTER para continuar.")

            
            elif resp3 == '2':
                resp4 = ''
                while resp4 != '0':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print()
                    print("###############################################")
                    print("######   Relatório de dados de Produtos   #####")
                    print("###############################################")
                    print()
                    print('''
                            #### 1 - CNPJ do cliente.
                            #### 2 - Produto pedido.
                            #### 3 - Periodo.
                            #### 5 - Status (ativo ou inativo).
                        ''')
                    resp4 = input("#### A partir de qual informação deseja começar sua busca?")
                    
                    
                    if resp4 == '1':
                       os.system('cls' if os.name == 'nt' else 'clear')
                       print()
                       print("############################################")
                       print("######       Relatório CNPJ       ####")
                       print("############################################")
                       print()
                       cnpj_pro = input("#### Insira o CNPJ que procura: ")
                       encontrou = False
                       print()

                       for num_pedido, dados in pedidos.items():
                          cnpj = dados[0]
                          
                          if cnpj.startswith(cnpj_pro.lower()):
                             print("ID do Pedido: ", num_pedido)
                             print("CNPJ do cliente: ", dados[0])
                             print("ID do Produto pedido", dados[1])
                             print("Quantidade pedida: ", dados[2])
                             print("Data do Pedido: ", dados[3])
                             print("Status do Pedido: ", dados[4])
                             print("--------------------------------------")
                             encontrou = True

                       if encontrou == False:
                        print("CNPJ não encontrado!")

                        print()
                        input("#### Pressione ENTER para continuar.")

                    
                    elif resp4 == '2':
                       os.system('cls' if os.name == 'nt' else 'clear')
                       print()
                       print("############################################")
                       print("######       Relatório CNPJ       ####")
                       print("############################################")
                       print()
                       produto_pro = input("#### Insira o ID do Produto que procura: ")
                       encontrou = False
                       print()

                       for num_pedido, dados in pedidos.items():
                          cod_pro = dados[1]
                          
                          if cod_pro.startswith(cod_pro.lower()):
                             print("ID do Pedido: ", num_pedido)
                             print("CNPJ do cliente: ", dados[0])
                             print("ID do Produto pedido", dados[1])
                             print("Quantidade pedida: ", dados[2])
                             print("Data do Pedido: ", dados[3])
                             print("Status do Pedido: ", dados[4])
                             print("--------------------------------------")
                             encontrou = True

                       if encontrou == False:
                        print("ID não encontrado!")

                        print()
                        input("#### Pressione ENTER para continuar.")

                    
                    elif resp4 == '3':
                       os.system('cls' if os.name == 'nt' else 'clear')
                       print()
                       print("############################################")
                       print("######       Relatório CNPJ       ####")
                       print("############################################")
                       print()
                       data_ini = input("#### Insira a data inicial: (dd/mm/aa)")
                       data_fim = input("#### Insira a data final: (dd/mm/aa)")
                       encontrou = False
                       print()

                       data_inicial = datetime.strptime(data_ini, "%d/%m/%y")
                       data_final = datetime.strptime(data_ini, "%d/%m/%y")

                       for num_pedido, dados in pedidos.items():
                          data_pedido = dados[3]

                          data_ped = datetime.strptime(data_pedido, "%d/%m/%y")

                          if data_ped >= data_inicial and data_ped <= data_final:
                            print("ID do Pedido: ", num_pedido)
                            print("CNPJ do cliente: ", dados[0])
                            print("ID do Produto pedido", dados[1])
                            print("Quantidade pedida: ", dados[2])
                            print("Data do Pedido: ", dados[3])
                            print("Status do Pedido: ", dados[4])
                            print("--------------------------------------")
                            encontrou = True

                       if encontrou == False:
                        print("ID não encontrado!")

                        print()
                        input("#### Pressione ENTER para continuar.")

                    
                    elif resp4 == '4':
                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("############################################")
                        print("######       Relatório Status       ####")
                        print("############################################")
                        print()
                        status = input("#### Qual opção de status deseja ver? Ativos(1), Inativos(2): ")
                        encontrou = False
                        print()

                        for num_pedido, dados in pedidos.items():

                            if status == '1':
                                if dados[4] == True:
                                    print("ID do Pedido: ", num_pedido)
                                    print("CNPJ do cliente: ", dados[0])
                                    print("ID do Produto pedido", dados[1])
                                    print("Quantidade pedida: ", dados[2])
                                    print("Data do Pedido: ", dados[3])
                                    print("Status do Pedido: ", dados[4])
                                    print("--------------------------------------")
                                    encontrou = True

                            elif status == '2':
                                if dados[4] == False:
                                    print("ID do Pedido: ", num_pedido)
                                    print("CNPJ do cliente: ", dados[0])
                                    print("ID do Produto pedido", dados[1])
                                    print("Quantidade pedida: ", dados[2])
                                    print("Data do Pedido: ", dados[3])
                                    print("Status do Pedido: ", dados[4])
                                    print("--------------------------------------")
                                    encontrou = True

                            else:
                               print("#### Insira um valor válido!")

                        if encontrou == False:
                            print("Produto não encontrado!")

                        print()
                        input("#### Pressione ENTER para continuar.")
               

    elif resp == '5':
      resp2 == ''
      while resp2 != '0':
        os.system('cls' if os.name == 'nt' else 'clear')

        print('''
              ############################################
              ######  Informações sobre nós!  ############
              ############################################

              ######  Sistema de gerenciamento e controle de fábrica de chapéus e bonés  ####
              ######  Equipe de desenvolvimento:       ####
              ######  * Marcos Paulo   ####

        ''')
        
        input("#### Pressione ENTER para continuar.")

    elif resp == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Fim do programa!")

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida!")
        input("#### Pressione ENTER para continuar.")

print("Obrigado por preferir Gentildonnas Attelier!")


fun_clientes.grava_clientes(clientes)
fun_produtos.grava_produtos(produtos)
fun_pedidos.grava_pedidos(pedidos)