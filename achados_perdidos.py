import csv
import os

ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "achados_perdidos.csv")
ARQUIVO_EXCLUIDOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "objetos_excluidos.csv")
CAMPOS = ["nome", "descricao", "local", "data"]


def salvar_itens(itens):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(itens)


def carregar_itens():
    itens = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                itens.append(linha)
    return itens


def salvar_item_excluido(item, motivo):
    arquivo_existe = os.path.exists(ARQUIVO_EXCLUIDOS) and os.path.getsize(ARQUIVO_EXCLUIDOS) > 0
    with open(ARQUIVO_EXCLUIDOS, "a", newline="", encoding="utf-8") as arquivo:
        campos = CAMPOS + ["motivo_exclusao"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        if not arquivo_existe:
            escritor.writeheader()
        escritor.writerow({**item, "motivo_exclusao": motivo})


def listar_itens(itens):
    print("\n--- OBJETOS CADASTRADOS ---")
    if len(itens) == 0:
        print("Nenhum objeto cadastrado.")
        return
    for numero, item in enumerate(itens, start=1):
        print(f"\nObjeto {numero}")
        print(f"Nome: {item['nome']}")
        print(f"Descrição: {item['descricao']}")
        print(f"Local: {item['local']}")
        print(f"Data: {item['data']}")
        print("-" * 30)


def cadastrar_item(itens):
    print("\n--- CADASTRO DE OBJETO ---")
    nome = input("Nome do objeto: ")
    descricao = input("Descrição: ")
    local = input("Local encontrado: ")
    data = input("Data (dd/mm/aaaa): ")
    if nome.strip() == "":
        print("Nome obrigatório.")
        return
    if descricao.strip() == "":
        print("Descrição obrigatória.")
        return
    if local.strip() == "":
        print("Local obrigatório.")
        return
    if data.strip() == "":
        print("Data obrigatória.")
        return
    item = {"nome": nome, "descricao": descricao, "local": local, "data": data}
    itens.append(item)
    salvar_itens(itens)
    print("Objeto cadastrado com sucesso!")


def excluir_item(itens):
    print("\n--- EXCLUSÃO DE OBJETO ---")
    if len(itens) == 0:
        print("Nenhum objeto cadastrado.")
        return
    listar_itens(itens)
    try:
        numero = int(input("\nNúmero do objeto: "))
        if numero < 1 or numero > len(itens):
            print("Número inválido.")
            return
        item_escolhido = itens[numero - 1]
        print(f"Objeto: {item_escolhido['nome']}")
        motivo = input("Motivo da exclusão: ")
        if motivo.strip() == "":
            print("Motivo obrigatório.")
            return
        confirmacao = input("Confirmar exclusão? (S/N): ")
        if confirmacao.upper() == "S":
            salvar_item_excluido(item_escolhido, motivo)
            itens.pop(numero - 1)
            salvar_itens(itens)
            print("Objeto excluído com sucesso!")
        else:
            print("Exclusão cancelada.")
    except ValueError:
        print("Digite somente números.")


def mostrar_menu():
    print("\n================================")
    print(" ACHADOS E PERDIDOS DA ESCOLA")
    print("================================")
    print("1 - Cadastrar objeto")
    print("2 - Listar objetos")
    print("3 - Excluir objeto")
    print("4 - Sair")


def main():
    itens = carregar_itens()
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            cadastrar_item(itens)
        elif opcao == "2":
            listar_itens(itens)
        elif opcao == "3":
            excluir_item(itens)
        elif opcao == "4":
            print("\nPrograma encerrado.")
            break
        else:
            print("\nOpção inválida. Digite 1, 2, 3 ou 4.")


if __name__ == "__main__":
    main()
