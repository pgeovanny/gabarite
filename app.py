
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

DATABASE = 'gabarite.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT, cpf TEXT UNIQUE, email TEXT, senha TEXT,
                nascimento TEXT, estado TEXT, area_estudo TEXT, curso TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS questoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                enunciado TEXT, artigo TEXT, lei TEXT,
                dificuldade TEXT, tipo TEXT, resposta TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS respostas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER, questao_id INTEGER,
                correta BOOLEAN, data TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        nascimento = request.form['nascimento']
        estado = request.form['estado']
        area = request.form['area']
        curso = request.form['curso']
        senha = request.form['senha']
        email = request.form['email']
        with sqlite3.connect(DATABASE) as conn:
            try:
                conn.execute("INSERT INTO users (nome, cpf, nascimento, estado, area_estudo, curso, senha, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                             (nome, cpf, nascimento, estado, area, curso, senha, email))
                conn.commit()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                return "CPF já cadastrado!"
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form['cpf']
        senha = request.form['senha']
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.execute("SELECT id FROM users WHERE cpf=? AND senha=?", (cpf, senha))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0]
                return redirect(url_for('painel'))
            else:
                return "Login inválido!"
    return render_template('login.html')

@app.route('/painel')
def painel():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('painel.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
