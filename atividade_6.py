import tkinter as tk
contador = 0

def clicar():
    global contador
    contador += 1
    label.config(text=f"Botão clicado: {contador}")

root = tk.Tk()
root.title("Interatividade")

label = tk.Label(root, text="Clique no botão.")
label.pack()

botao = tk.Button(root, text="Clique aqui", command=clicar)
botao.pack()

root.mainloop()