
import tkinter as tk
# janela
janela = tk.Tk()
janela.title("Janela Simples")
janela.geometry("500x400")


def verificar():
    if opcao.get():
        print("selecinado")
    else:
        print("não selecionado!")
janela = tk.Tk()
janela.title("exemplo de caixa de seleção")
janela.geometry("500x400")
opcao= tk.IntVar()
check= tk.Checkbutton(janela,text="escolha uma opcão",variable=opcao, command=verificar )
check.pack(pady=20)
janela.mainloop()