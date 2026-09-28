import mysql.connector
from banco import conectar
from departamento import listar_departamento


def inserir_funcionario():
    nome = input("Nome do funcionário: ").strip()
    cargo = input("Cargo: ").strip()
    if not nome or not cargo:
        print("Nome e cargo são obrigatórios.")
        return
    try:
        salario = float(input("Salário: ").replace(",", "."))
    except ValueError:
        print("Salário inválido.")
        return

    listar_departamento()
    try:
        departamento_id = int(input("\nID do departamento: "))
    except ValueError:
        print("ID inválido.")
        return

    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "INSERT INTO funcionario(nome, cargo, salario, departamento_id) "
            "VALUES (%s, %s, %s, %s)",
            (nome, cargo, salario, departamento_id),
        )
        conexao.commit()
        print("Funcionário inserido com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao inserir (o departamento existe?): {erro}")
    finally:
        cursor.close()
        conexao.close()


def listar_funcionario():
    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "SELECT f.id, f.nome, f.cargo, f.salario, d.nome "
            "FROM funcionario f "
            "JOIN departamento d ON d.id = f.departamento_id "
            "ORDER BY f.id"
        )
        registros = cursor.fetchall()
        if not registros:
            print("Nenhum funcionário cadastrado.")
            return
        print(f"\n{'ID':<4}| {'NOME':<25}| {'CARGO':<20}| {'SALÁRIO':<12}| DEPARTAMENTO")
        print("-" * 80)
        for id_, nome, cargo, salario, depto in registros:
            print(f"{id_:<4}| {nome:<25}| {cargo:<20}| {salario:<12.2f}| {depto}")
    except mysql.connector.Error as erro:
        print(f"Erro ao consultar: {erro}")
    finally:
        cursor.close()
        conexao.close()


def atualizar_funcionario():
    listar_funcionario()
    try:
        id_ = int(input("\nDigite o ID do funcionário que deseja alterar: "))
    except ValueError:
        print("ID inválido.")
        return
    nome = input("Novo nome: ").strip()
    cargo = input("Novo cargo: ").strip()
    if not nome or not cargo:
        print("Nome e cargo são obrigatórios.")
        return
    try:
        salario = float(input("Novo salário: ").replace(",", "."))
    except ValueError:
        print("Salário inválido.")
        return

    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "UPDATE funcionario SET nome = %s, cargo = %s, salario = %s WHERE id = %s",
            (nome, cargo, salario, id_),
        )
        conexao.commit()
        if cursor.rowcount == 0:
            print("Funcionário não encontrado (ou nenhum dado foi alterado).")
        else:
            print("Funcionário atualizado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar: {erro}")
    finally:
        cursor.close()
        conexao.close()


def excluir_funcionario():
    listar_funcionario()
    try:
        id_ = int(input("\nDigite o ID do funcionário que deseja excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    conexao = conectar()
    if conexao is None:
        return
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM funcionario WHERE id = %s", (id_,))
        conexao.commit()
        if cursor.rowcount == 0:
            print("Funcionário não encontrado.")
        else:
            print("Funcionário excluído com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro ao excluir: {erro}")
    finally:
        cursor.close()
        conexao.close()
