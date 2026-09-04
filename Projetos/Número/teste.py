from tkinter import *
import tkinter as tk

class Cronometro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Contador de Horas")
        self.janela.geometry('1100x800')

        janela.columnconfigure(0, weight=1)
        janela.columnconfigure(1, weight=3)

        janela.rowconfigure(1, weight=2)

        sidebar = tk.Frame(janela, bg="red")
        sidebar.grid(row=1, column=0, sticky='nsew')

        acentral = tk.Frame(janela, bg='blue')
        acentral.grid(row=1, column=1, sticky='nsew')

if __name__ == "__main__":
    janela = Tk()
    app = Cronometro(janela)
    janela.mainloop()
