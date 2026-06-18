# 🫀 Sistema de Gestão de Órgão 🫀

Este é um sistema de controle de inventário desenvolvido em Python focado no gerenciamento e armazenamento. O projeto resolve o desafio de salvamento das atualizações, garantindo que as informações inseridas na memória não sejam perdidas ao fechar o programa.

## ⚠️ Funcionalidades Principais

*  Cria e atualiza o arquivo `estoque.txt` sempre que houver alterações nos dados.
*  Carrega todo o histórico salvo assim que o sistema inicia.
*  Permite cadastrar, listar, buscar por ID, atualizar quantidades e remover registros.
*  Calcula em tempo real o valor total de mercado baseado nas quantidades disponíveis.
*  Notifica os administradores quando o estoque de algum item está abaixo de 5 unidades.

---

## 🛠️ Tecnologias Usadas

O sistema utiliza os conceitos fundamentais da programação estruturada em Python:

1.  Matrizes (Listas de Listas): Cada órgão é mapeado internamente com a estrutura `[ID, Nome, Quantidade, Localização, Preço]`.
2.  Manipulação de Arquivos (`open()`):
    *   **Escrita (`"w"`):** Transforma os dados da matriz em texto separado por ponto e vírgula (`;`) e salva no disco.
    *   **Leitura (`"r"`):** Lê cada linha do arquivo de texto, reconverte os tipos primitivos (`int` e `float`) e reconstrói a matriz original.
3.  Controle de Fluxo Iterativo: Laço principal `while True` com validação de opções via menu numérico.

## 📂 Como Executar o Projeto

Siga os passos abaixo para rodar o sistema localmente:

1. Clone o repositório para a sua máquina:
   ```bash
   git clone https://github.com/rayanesantos16/PROJETO---Log-stica.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd PROJETO-Logistica
   ```

3. Execute o script principal:
   ```bash
   python SCES.py
   ```
> 💡 **Nota:** O arquivo `estoque.txt` será criado de forma 100% automática na mesma pasta logo após a primeira inserção ou alteração de dados.
