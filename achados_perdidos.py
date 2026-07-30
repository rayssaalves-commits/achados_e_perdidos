def mostrar_menu():
print("\n================================")
print(" ACHADOS E PERDIDOS DA ESCOLA")
print("================================")
print("1 - Cadastrar objeto")
print("2 - Listar objetos")
print("3 - Excluir objeto")
print("4 - Sair")

def main():
mostrar_menu()
opcao = input("\nEscolha uma opção: ")
print("Você escolheu a opção:", opcao)
main()

# FUNÇÃO RESPONSÁVEL POR MOSTRAR O MENU
def mostrar_menu():
# Mostra uma linha em branco antes do menu.
print("\n================================")
# Mostra o título do sistema.
print(" ACHADOS E PERDIDOS DA ESCOLA")
# Mostra outra linha para organizar visualmente.
print("================================")
# Mostra as opções disponíveis no programa.
print("1 - Cadastrar objeto")
print("2 - Listar objetos")
print("3 - Excluir objeto")
print("4 - Sair")
