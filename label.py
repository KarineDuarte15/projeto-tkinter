import tkinter as tk
# janela
janela = tk.Tk()
janela.title("Janela Simples")
janela.geometry("500x400")

# Label
label = tk.Label(janela, text="Olá, mundo!")
label.pack(pady=50)
janela.mainloop()