# Projeto Empresa

Sistema de terminal em Python para cadastrar **departamentos** e **funcionários**
em um banco MySQL, com as quatro operações CRUD.

## Estrutura

```
empresa/
├── banco.py            # conexão com o MySQL
├── departamento.py     # CRUD de departamento
├── funcionario.py      # CRUD de funcionário
├── menu.py             # ponto de entrada (menus)
├── criar_tabelas.sql   # script do banco
└── requirements.txt    # dependências
```

## Pré-requisitos

- Python 3.13
- MySQL rodando (XAMPP/WAMP), usuário `root` sem senha (ajuste em `banco.py` se for diferente)

## Instalação

1. Abra o phpMyAdmin, vá na aba **SQL**, cole o conteúdo de `criar_tabelas.sql` e execute.
2. No terminal, dentro da pasta do projeto:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Execução

```
python menu.py
```

## Como usar

```
SISTEMA EMPRESA
1 - DEPARTAMENTO   -> inserir, consultar, atualizar, excluir
2 - FUNCIONÁRIO    -> inserir, consultar, atualizar, excluir
0 - SAIR
```

Cadastre primeiro os departamentos: todo funcionário precisa pertencer a um.

## Publicar no GitHub

```
git init
git add .
git commit -m "Projeto Empresa"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/empresa.git
git push -u origin main
```
