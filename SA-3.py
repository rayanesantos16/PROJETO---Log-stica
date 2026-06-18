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
