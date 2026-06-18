estoque = []
proximo_id= 1

def adicionar_produto():
    global proximo_id
    print("\n===== ADICIONAR PRODUTO =====")
    produto_id = int(input("Digite o ID do produto (apenas números): "))
    
    id_existe = False
    for produto in estoque:
        if produto[0] == produto_id:
            id_existe = True

    if id_existe:
        print("Já existe um produto com este ID.")
    else:
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade de produtos: "))
        localizacao = input("Digite a localização do produto (ex: A34): ")
        preco = float(input("Digite o preço unitário do produto (ex: 10.50): "))

        novo_produto = [produto_id, nome, quantidade, localizacao, preco]
        estoque.append(novo_produto)
        print("Produto cadastrado com êxito!")

def listar_produtos():
    print("\n===== LISTA DE PRODUTOS =====")
    if len(estoque) == 0:
        print("O estoque está vazio.")
    else:
        print("ID        | Nome                      | Qtd        | Localização     | Preço (R$)")
        print("==========================================================================================")

        for p in estoque:
            print(f"{p[0]:<9} | {p[1]:<25} | {p[2]:<10} | {p[3]:<15} | R$ {p[4]:.2f}")

def buscar_produto():
    print("\n===== BUSCAR PRODUTO POR ID =====")
    produto_id = int(input("Digite o ID do produto que deseja buscar: "))

    achou = False
    for produto in estoque:
        if produto[0] == produto_id:
            print("\n===== Produto Encontrado =====")
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Quantidade: {produto[2]}")
            print(f"Localização: {produto[3]}")
            print(f"Preço Unitário: R$ {produto[4]:.2f}")
            achou = True

    if not achou:
        print("Produto não está no estoque.")

def atualizar_estoque():
    print("\n===== ATUALIZAR ESTOQUE =====")
    produto_id = int(input("Digite o ID do produto: "))

    achou = False
    for i in range(len(estoque)):
        if estoque[i][0] == produto_id:
            achou = True
            
            produto_removido = estoque.pop(i)
            
            id_produto = produto_removido[0]
            nome_produto = produto_removido[1]
            quantidade_p = produto_removido[2]
            local_produto = produto_removido[3]
            preco_produto = produto_removido[4] 

            print(f"Produto selecionado: {nome_produto} (Quantidade atual: {quantidade_p})")
            print("1. Entrada (+)")
            print("2. Saída (-)")
            opcao = input("Escolha uma operação: ")
            quantidade_alterar = int(input("Digite a quantidade: "))

            if opcao == '1':
                quantidade_p = quantidade_p + quantidade_alterar
                print(f" Nova quantidade: {quantidade_p}")
            elif opcao == '2':
                if quantidade_p >= quantidade_alterar:
                    quantidade_p = quantidade_p - quantidade_alterar
                    print(f" Nova quantidade: {quantidade_p}")
                else:
                    print("Estoque insuficiente.")
            else:
                print("Opção inválida.")

            produto_atualizado = [id_produto, nome_produto, quantidade_p, local_produto, preco_produto]
            estoque.insert(i, produto_atualizado)
            break

    if not achou:
        print("Produto não esta no estoque.")

def calcular_valor_inventario():
    print("\n===== VALOR TOTAL DO INVENTÁRIO =====")
    if len(estoque) == 0:
        print("O estoque está vazio. O valor total é R$ 0.00")
    else:
        valor_total_geral = 0.0
        
        print("Resumo Financeiro por Item:")
        print("==========================================================================================")
        for p in estoque:
            valor_item = p[2] * p[4]
            valor_total_geral = valor_total_geral + valor_item
            print(f"Produto: {p[1]:<20} | Valor em Estoque: R$ {valor_item:.2f}")
            
        print("==========================================================================================")
        print(f"VALOR TOTAL ACUMULADO: R$ {valor_total_geral:.2f}")


def travamenu():
    input("\nPressione <ENTER> para continuar...")

print("🌟Bem vindo ao menu!🌟")
while True:
    print("\nPor favor, selecione uma opção:")
    print(" | 1- Adicionar produto \n| 2- Listar produtos \n| 3- Buscar produto \n| 4- Atualizar estoque \n| 5- Calcular Valor do Inventário \n| 6- Sair")
    opção = input("Escolha: ")
    
    if opção == "1":
        adicionar_produto()
        travamenu()
    elif opção == "2":
        listar_produtos()
        travamenu()
    elif opção == "3":
        buscar_produto()
        travamenu()
    elif opção == "4":
        atualizar_estoque()
        travamenu()
    elif opção == "5":
        calcular_valor_inventario()
        travamenu()
    elif opção == "6":
        print("Menu encerrado...")
        break
    else:
        print("Tente novamente.")
