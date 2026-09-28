from departamento import (
    inserir_departamento,
    listar_departamento,
    atualizar_departamento,
    excluir_departamento,
)
from funcionario import (
    inserir_funcionario,
    listar_funcionario,
    atualizar_funcionario,
    excluir_funcionario,
)


def menu_departamento():
    while True:
        print("\n=============================")
        print("DEPARTAMENTO")
        print("=============================")
        print("1 - INSERIR")
        print("2 - CONSULTAR")
        print("3 - ATUALIZAR")
        print("4 - EXCLUIR")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir_departamento()
        elif opcao == "2":
            listar_departamento()
        elif opcao == "3":
            atualizar_departamento()
        elif opcao == "4":
            excluir_departamento()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_funcionario():
    while True:
        print("\n=============================")
        print("FUNCIONÁRIO")
        print("=============================")
        print("1 - INSERIR")
        print("2 - CONSULTAR")
        print("3 - ATUALIZAR")
        print("4 - EXCLUIR")
        print("0 - VOLTAR")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir_funcionario()
        elif opcao == "2":
            listar_funcionario()
        elif opcao == "3":
            atualizar_funcionario()
        elif opcao == "4":
            excluir_funcionario()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_principal():
    while True:
        print("\n=============================")
        print("SISTEMA EMPRESA")
        print("=============================")
        print("1 - DEPARTAMENTO")
        print("2 - FUNCIONÁRIO")
        print("0 - SAIR")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_departamento()
        elif opcao == "2":
            menu_funcionario()
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
