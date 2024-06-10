import sqlite3

# criando conexão
try:
    con = sqlite3.connect('casdastro_aluno.db')
    print('Conexão com o banco de dados realizada com sucesso!')
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

# Tabela de Cursos -------------------------------------------------

# Criar cursos (CREATE C )
def criar_cursos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?, ?, ?)"
        cur.execute(query, i)

# Ver todos os cursos ( READ R )
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

# Atualizar os Cursos (Update U)
def atualizar_cursos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query, i)

# Deletar os cursos (Delete D)
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query, i)

# Tabela de Turmas -------------------------------------------------

# Criar turmas (Creat C)
def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas (nome, curso_nome, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)

# Ver todas as Turmas (Read R)
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)

    return lista

# Atualizar as Turmas (Update U)
def atualizar_turmas(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
        cur.execute(query, i)

# Deletar as Turmas (Delete D)
def deletar_turma(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Turmas WHERE id=?"
        cur.execute(query, i)


# Tabela de Alunos -------------------------------------------------

# Criar alunos (Creat C)
def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = '''INSERT INTO alunos2 (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        cur.execute(query, i)

# Ver Alunos (Read R)
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM alunos2')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

# Atualizar Alunos (Update U)
def atualizar_alunos (i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos2 SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
        cur.execute(query, i)


# Deletar Alunos (Delete D)
def deletar_aluno(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM alunos2 WHERE id=?"
        cur.execute(query, i)
