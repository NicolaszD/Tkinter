import tkinter as tk

def enviar():
    nome = entrada.get()
    label_resultado.config(text=f"Olá, {nome}.")

root = tk.Tk()
root.geometry("500x300")
root.title("Digite seu Nome")

entrada = tk.Entry(root)
entrada.pack()

botao = tk.Button(root, text="Enviar", command=enviar)
botao.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop()

