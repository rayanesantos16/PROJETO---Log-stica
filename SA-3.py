estoque = [
    [1, "Coração Humano", 3, "Câmara Fria A", 650.000,00],
    [2, "Rim Humano", 8, "Câmara Fria B",27.000,00 ],
    [3, "Útero Humano", 2, "Maleta Térmica 01", 500.000,00],
    [4, "Fígado Humano", 6, "Câmara Fria C", 68.000,00],
    [5, "Pulmão Humano", 4, "Câmara Fria D", 64.000,00]
]

proximo_id = 6

def adicionar_produto():
    global proximo_id
    print("\n====== CADASTRAR NOVO ÓRGÃO ========")
    nome = input("Nome do Órgão/Item: ")
    quantidade = int(input("Quantidade em Estoque: "))
    localizacao = input("Câmara de Armazenamento: ")
    preco = float(input("Preço (R$): "))
    
    estoque.append([proximo_id, nome, quantidade, localizacao, preco])
    print(f"Cadastrado com sucesso! ID gerado automaticamente: {proximo_id}")
    proximo_id +=1

def listar_produtos():
    print("\n===== INVENTÁRIO DE ÓRGÃOS =====")
    if len(estoque) == 0:
        print("Estoque vazio.")
    else:
        for p in estoque:
            print(f"ID: {p[0]} | Item: {p[1]} | Qtd: {p[2]} | Local: {p[3]} | Preço: R$ {p[4]:.2f}")

def buscar_produto():
    print("\n===== BUSCAR ÓRGÃO POR ID =====")
    id_busca = int(input("Digite o ID do órgão: "))
    achou = False
    for p in estoque:
        if p[0] == id_busca:
            print(f"ID: {p[0]} | Item: {p[1]} | Qtd: {p[2]} | Local: {p[3]} | Preço: R$ {p[4]:.2f}")
            achou = True
            break
    if not achou:
        print("Órgão não encontrado no sistema.")

def atualizar_estoque():
    print("\n--- ATUALIZAR QUANTIDADE DE ÓRGÃOS =====")
    id_busca = int(input("Digite o ID do órgão: "))
    achou = False
    for i in range(len(estoque)):
        if estoque[i][0] == id_busca:
            achou = True
            print(f"Item: {estoque[i][1]} | Quantidade Atual: {estoque[i][2]}")
            print("1 - Entrada (+)\n2 - Saída (-)")
            opcao = input("Opção: ")
            qtd_alterar = int(input("Quantidade a alterar: "))
            
            if opcao == "1":
                estoque[i][2] = estoque[i][2] + qtd_alterar
                print("Quantidade atualizada com sucesso.")
            elif opcao == "2":
                if estoque[i][2] >= qtd_alterar:
                    estoque[i][2] = estoque[i][2] - qtd_alterar
                    print("Retirada realizada com sucesso.")
                else:
                    print("Erro: Estoque insuficiente para essa retirada.")
            else:
                print("Opção inválida.")
            break
    if not achou:
        print("Órgão não encontrado.")

def calcular_valor_inventario():
    print("\n===== BALANÇO FINANCEIRO DO ESTOQUE =====")
    total = 0.0
    for p in estoque:
        valor_item = p[2] * p[4]
        total = total + valor_item
        print(f"{p[1]}: R$ {valor_item:.2f}")
    print(f"VALOR TOTAL DO MERCADO: R$ {total:.2f}")

def verificar_estoque_minimo():
    print("\n===== ALERTA DE ESTOQUE MÍNIMO =====")
    alerta = False
    for p in estoque:
        if p[2] < 5:
            print(f"⚠️ Alerta: {p[1]} em nível crítico! Apenas {p[2]} unidades no {p[3]}.")
            alerta = True
    if not alerta:
        print("Todos os órgãos estão com níveis seguros de armazenamento.")

def remover_produto():
    print("\n===== EXCLUSÃO DEFINITIVA DE REGISTRO =====")
    id_remover = int(input("Digite o ID do órgão a ser descartado: "))
    achou = False
    for i in range(len(estoque)):
        if estoque[i][0] == id_remover:
            orgao_removido = estoque.pop(i)
            print(f"Registro '{orgao_removido[1]}' removido definitivamente da matriz.")
            achou = True
            break
    if not achou:
        print("Órgão não encontrado para remoção.")

while True:
    print("\n======= SISTEMA ORGÃOS EM ESTOQUE =======")
    print("| 1-Cadastrar Órgão \n| 2-Listar Estoque \n| 3-Buscar por ID \n| 4-Atualizar Quantidade ")
    print("| 5-Valor Total     \n| 6-Nível Baixo de Estoque \n| 7-Retirar Item \n| 8-Sair")
    op = input("Escolha a operação: ")
    
    if op == "1":
        adicionar_produto()
    elif op == "2":
        listar_produtos()
    elif op == "3":
        buscar_produto()
    elif op == "4":
        atualizar_estoque()
    elif op == "5":
        calcular_valor_inventario()
    elif op == "6":
        verificar_estoque_minimo()
    elif op == "7":
        remover_produto()
    elif op == "8":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida do menu.")