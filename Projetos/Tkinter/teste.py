from tkinter import *
import tkinter as tk

class Cronometro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Contador de Horas")
        self.janela.geometry('1100x800')

        janela.columnconfigure(0, weight=2)
        janela.columnconfigure(1, weight=3)

        janela.rowconfigure(1, weight=2)

        sidebar = tk.Frame(janela, bg="#666660")
        sidebar.grid(row=1, column=0, sticky='nsew')

        self.acentral = tk.Frame(janela, bg="#020202")
        self.acentral.grid(row=1, column=1, sticky='nsew')

        self.interface()

    def interface(self):
        self.acentral.columnconfigure(0, weight=1)
        self.acentral.rowconfigure(0, weight=1)
        container = Frame(self.acentral, bg="#464646", width=700, height=500, highlightthickness=2.5, highlightbackground="#ffffff")
        container.grid(row=0, column=0)
        

if __name__ == "__main__":
    janela = Tk()
    app = Cronometro(janela)
    janela.mainloop()
