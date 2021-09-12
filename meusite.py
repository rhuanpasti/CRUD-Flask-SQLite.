from flask import Flask, render_template, request

import sqlite3
import os
import os.path

app = Flask(__name__)

def db_inserir(titulo,ano,autor,editora):
    return """
    INSERT INTO livros (titulo, ano, autor, editora)
    VALUES('{}', '{}', '{}', '{}')
    """.format(titulo, ano, autor, editora)
    return meusite.py


def db_editar(id, titulo, ano, autor, editora):
    return """
    UPDATE livros  SET ano = '{}', autor ='{}', editora ='{}', titulo ='{}' WHERE id='{}'
    """.format(ano, autor, editora, titulo, id)
    return meusite.py

def db_deletar(id):
    return """
    DELETE FROM livros WHERE id='{}'
    """.format(id)
    

def db_busca(oque, onde):
    return """
    SELECT id, titulo, ano, autor, editora
    FROM livros
    WHERE {} = {}""".format(oque, onde)

@app.route("/")
def main():
    con = conectarDB()
    livros = con.execute('SELECT * FROM livros').fetchall()
    con.close()
    return render_template('index.html', livros=livros)

@app.route("/pagcadastro")
def pagcadastro():
    return render_template('pag.html')
    
@app.route('/editar', methods = ['GET','POST'])
def editar():
    con = sqlite3.connect('books.db')
    cur = con.cursor()

    id = request.form.get('id')
    titulo = request.form.get("titulo")
    ano = request.form.get("ano")
    autor = request.form.get("autor")
    editora = request.form.get("editora")

    cur.execute(db_editar(id ,titulo, ano, autor, editora))

    con.commit()
    return main()

@app.route("/pagpesquisar")
def pesquisar():
     return main()

@app.route('/<int:id>/excluir')
def excluir(id):
    con = sqlite3.connect('books.db')
    cur = con.cursor()
    print(id)
    cur.execute(db_deletar(id))
    con.commit()
    return main()

@app.route("/pag", methods = ["POST"])
def adicionar():
    
    con = sqlite3.connect('books.db')
    cur = con.cursor()

    titulo = request.form.get("titulo")
    ano = request.form.get("ano")
    autor = request.form.get("autor")
    editora = request.form.get("editora")

    print(titulo, ano, autor, editora)

    cur.execute(db_inserir(titulo, ano, autor, editora))
    con.commit()
    return main()

def conectarDB():
    con = sqlite3.connect('books.db')
    cur = con.cursor()
    con.row_factory = sqlite3.Row
    return con







    

   







