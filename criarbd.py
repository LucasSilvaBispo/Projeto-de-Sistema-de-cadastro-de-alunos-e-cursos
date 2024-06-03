# importando SQLite 3
import sqlite3

# criando conexão
try:
    con = sqlite3.connect('casdastro_aluno.db')
    print('Conexão com o banco de dados realizada com sucesso!')
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

# Criando tabela de cursos
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            duracao TEXT,
            preco REAl            
            )""")
        print("Tabela Cursos criado com sucesso")

except sqlite3.Error as e:
    print("Erro ao criar a tabela de cursos:", e)

# Criando tabela de Turmas
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            curso_nome TEXT,
            data_inicio DATE,
            FOREIGN KEY (curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        print("Tabela turmas criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela de turmas', e)

# Criando tabela de Alunos
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS alunos2(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            sexo TEXT,
            imagem TEXT,
            data_nascimento DATE,
            cpf TEXT,
            turma_nome TEXT,
            FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE                    
       )""")
        print("Tabela Alunos criada com sucesso!")
except sqlite3.Error as e:
    print('Erro ao criar a tabela Alunos', e)