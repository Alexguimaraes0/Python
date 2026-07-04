import tkinter as tk

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
resposta_num = numero1 + numero2

janela = tk.Tk()

#define o titulo da janela
janela.title('Calculadora')

#Define o tamanho que ira abrir
janela.geometry('400x500') # largura x altura

texto2 = tk.Label(janela, text=f'Bem vindo')
texto2.pack()

def usuario():
    nome = entrada_texto.get()
    texto2['text'] = f'Olá, {nome}'

entrada_texto = tk.Entry(janela)
entrada_texto.pack()

tk.Button(janela, text=('Definir Usuário'), command=usuario).pack()


#Exibir texto
texto = tk.Label(janela, text=f'O resultado da soma de {numero1} + {numero2} é de:')
texto.pack()


def resposta_botão():
    texto['text'] = f'Resultado: {resposta_num}'    

#Criar um botão
tk.Button(janela, text=('Somar'), command=resposta_botão).pack()

#Iniciar o loop principal (mantém a janela aberta)
janela.mainloop()