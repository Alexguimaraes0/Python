import tkinter as tk

janela = tk.Tk()
janela.title("Contador de horas")

titulo = tk.Label(janela, text="Contador de tempo")
titulo.pack()

sidebar = tk.Frame(janela, width=150, bg="red")
sidebar.pack(side=tk.LEFT, fill=tk.Y)

acentral = tk.Frame(janela, bg="Blue")
acentral.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

janela.mainloop()