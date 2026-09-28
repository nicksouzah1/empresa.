import mysql.connector
from banco import conectar


def inserir_departamento():
    nome = input("Digite o nome do departamento: ").strip()
    if not nome:
        print("O nome não pode ficar vazio.")
        return

    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO departamento(nome) VALUES (%s)", (nome,))
        conexao.commit()
        print("Departamento inserido com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao inserir: {erro}")
    finally:
        cursor.close()
        conexao.close()


def listar_departamento():
    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT id, nome FROM departamento ORDER BY id")
        registros = cursor.fetchall()
        if not registros:
            print("Nenhum departamento cadastrado.")
            return
        print("\nID  | NOME")
        print("-" * 30)
        for id_, nome in registros:
            print(f"{id_:<3} | {nome}")
    except mysql.connector.Error as erro:
        print(f"Erro ao consultar: {erro}")
    finally:
        cursor.close()
        conexao.close()


def atualizar_departamento():
    listar_departamento()
    try:
        id_ = int(input("\nDigite o ID do departamento que deseja alterar: "))
    except ValueError:
        print("ID inválido.")
        return
    nome = input("Digite o novo nome: ").strip()
    if not nome:
        print("O nome não pode ficar vazio.")
        return

    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    try:
        cursor.execute("UPDATE departamento SET nome = %s WHERE id = %s", (nome, id_))
        conexao.commit()
        if cursor.rowcount == 0:
            print("Departamento não encontrado.")
        else:
            print("Departamento atualizado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar: {erro}")
    finally:
        cursor.close()
        conexao.close()


def excluir_departamento():
    listar_departamento()
    try:
        id_ = int(input("\nDigite o ID do departamento que deseja excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM departamento WHERE id = %s", (id_,))
        conexao.commit()
        if cursor.rowcount == 0:
            print("Departamento não encontrado.")
        else:
            print("Departamento excluído com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Não foi possível excluir (há funcionários neste departamento?): {erro}")
    finally:
        cursor.close()
        conexao.close()
