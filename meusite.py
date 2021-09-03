from flask import Flask, render_template, request

import sqlite3
import os
import os.path



currentdirectory = os.path.dirname(os.path.abspath(__file__))



app = Flask(__name__)

@app.route("/page", methods=['GET', 'POST'])
def addpage():
    if request.method == 'POST':
        return render_template('index.html')

    # show the form, it wasn't submitted
    return render_template('pag.html')

@app.route("/")
def main():

    return render_template("index.html")


@app.route("/pag", methods=['POST'])
def pag():
    titulo = request.form["titulo"]
    ano = request.form["ano"]
    autor = request.form["autor"]
    editora = request.form ["editora"]
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, 'livros.db')
    with sqlite3.connect(db_path) as db:    
        conexao = db.cursor()
        conexao.execute ("INSERT INTO livros (titulo,ano,autor,editora) VALUES (?,?,?,?)", (titulo,ano,autor,editora))
    return render_template("index.html")
   







