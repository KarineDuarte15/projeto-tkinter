import tkinter as tk
janela = tk.Tk()
janela.title("janela principal")
janela.geometry("500x500")



label= tk.Label(janela,text="teste")
label.pack(pady=20)

janela.mainloop()