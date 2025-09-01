
import tkinter as tk

def clicar():
    label.config(text="Botão clicado!")

root = tk.Tk()
root.title("Interatividade")

label = tk.Label(root, text="Clique no botão.")
label.pack()

botao = tk.Button(root, text="Clique aqui", command=clicar)
botao.pack()

root.mainloop()
