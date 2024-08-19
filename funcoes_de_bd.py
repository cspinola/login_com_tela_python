import sqlite3

# Conectar-se a um ou criar um banco de dados
def conectar_db(nome_db):
    conexao = sqlite3.connect(nome_db)
    return conexao

def desconecta_bd(nome_db):
        nome_db.close()

# Criar tabela
def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuarios (
            login VARCHAR(25) PRIMARY KEY,
            senha VARCHAR(250)  NOT NULL
        );
    ''')
    conexao.commit()

# Inserir dados em uma tabela
def inserir_usuario(conexao, login, senha):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Usuarios VALUES (?, ?)",
                   (login, senha))
    conexao.commit()


def buscar_usuario(conexao, login, senha):
    cursor = conexao.cursor()
    cursor.execute(f"SELECT login FROM Usuarios WHERE senha = {senha}")
    return cursor.fetchall()

# Alterar dados de uma tabela

def atualizar_usuario(conexao, login, senha):
    cursor = conexao.cursor()
    cursor.execute("UPDATE Usuarios SET senha = ? WHERE id = ?",
                   (senha, login))
    conexao.commit()

# Como excluir dados de uma tabela

def deletar_usuario(conexao, login):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id = ?", (id,))
    conexao.commit()