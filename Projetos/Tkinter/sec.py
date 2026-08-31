import tkinter as tk

janela = tk.Tk()
janela.title("Contador de horas")
janela.geometry('1100x800')
janela.minsize(700,500)

janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=3)

janela.rowconfigure(2, weight=2)

titulo = tk.Label(janela, text="Contador de tempo")
titulo.grid(row=0, column=0, columnspan=2)

sidebar = tk.Frame(janela, bg="red")
sidebar.grid(row=1, column=0, sticky='nsew')

acentral = tk.Frame(janela, bg="Blue")
acentral.grid(row=1, column=1, sticky='nsew')

start = 0
rodando = False # pra saber se o timer tá ativo

def iniciar_timer():
    global start, rodando
    start = 'time'.time()
    rodando = True
    atualizar_timer() # já chama a primeira vez

def atualizar_timer():
    global rodando
    if rodando:
        decorrido = 'time'.time() - start

        # atualiza o label aqui com o valor de 'decorrido'
        janela.after(1000, 'atualizar_time')

janela.mainloop()