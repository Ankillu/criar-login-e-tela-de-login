from tkinter import Tk
import tkinter as tk
import sqlite3

conn = sqlite3.connect("contas.db")
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS usuarios (nome TEXT, senha INTEGER)''')
conn.commit()
conn.close()


janela = tk.Tk()
janela.wm_title("Criar Conta")
janela.geometry("256x256")
janela.config(background="#676967")
entrada_de_nome = tk.Entry(janela)
entrada_de_nome.pack()
entrada_de_senha = tk.Entry(janela)
entrada_de_senha.pack()


def enviar():
    nome = entrada_de_nome.get()
    senha = entrada_de_senha.get()
    conn = sqlite3.connect("contas.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
    conn.commit()
    conn.close()
    janela.destroy()

    janela1.wm_title("Login")
    janela1.geometry("256x256")
    janela1.config(background="#676967")

    entrada_de_nome_login.pack()
    entrada_de_senha_login.pack()
    botão_de_confirmar_login.pack()



def verificar_login():

    nome1 = entrada_de_nome_login.get()
    senha1 = entrada_de_senha_login.get()
    conn = sqlite3.connect("contas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome1, senha1))
    user = cursor.fetchall()
    if user:
        usuario_enc = tk.Label(janela1, text="Usuario encontrado")
        usuario_enc.pack()
    else:
        usuario_n_enc = tk.Label(janela1, text="Usuario não encontrado")
        usuario_n_enc.pack()

    janela1.mainloop()


botão_de_confirmar = tk.Button(
    janela, text="clique aqui pra confirmar", command=enviar)
botão_de_confirmar.pack()
janela1 = tk.Tk()
entrada_de_nome_login = tk.Entry(janela1)
entrada_de_senha_login = tk.Entry(janela1)
botão_de_confirmar_login = tk.Button(janela1, text="clique aqui pra confirmar", command=verificar_login)



janela.mainloop()
