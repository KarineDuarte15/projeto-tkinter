import tkinter as tk

# Button

def ao_clicar():
    print("Clicou no botão!")
janela = tk.Tk()
janela.title("Janela Simples")
janela.geometry("500x400")
button = tk.Button(janela, text="Clique aqui", command=janela.ao_clicar)
ao_clicar= tk.IntVar()
check= tk.Checkbutton(janela,text="escolha uma opcão",variable=janela, command=ao_clicar )
button.pack(pady=50)
button = tk.Button(janela, text="Fechar", command=janela.quit)
button.pack(pady=50)




janela.mainloop()
