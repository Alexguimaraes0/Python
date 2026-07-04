import tkinter as tk

contas = [
    ("alex", "123"),
    ("luffy", "carne")
]

janela = tk.Tk()
janela.title("Login")
janela.geometry("400x300")

pagina_login = tk.Frame(janela)
pagina_login.pack()

tk.Label(pagina_login, text='Usuário').pack()
usuario_entry = tk.Entry(pagina_login)
usuario_entry.pack()

tk.Label(pagina_login, text="Senha").pack()
senha_entry = tk.Entry(pagina_login)
senha_entry.pack()

def login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    if (usuario, senha) in contas:
        pagina_login.pack_forget()
        pagina_sistema.pack()
    else:
        mensagem['text'] = "Usuário ou senha invalida"       

tk.Button(pagina_login, text="Login", command=login).pack()

mensagem = tk.Label(pagina_login)
mensagem.pack()

pagina_sistema = tk.Frame()
tk.Label(pagina_sistema, text="Bem Vindo ao Sistema!").pack()


janela.mainloop()