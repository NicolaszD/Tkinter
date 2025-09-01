import tkinter as tk

def atualizar_texto(mensagem):
    label.config(text=mensagem)

root = tk.Tk()
root.title("Mensagens")

label = tk.Label(root, text="Escolha uma opção")
label.pack()

tk.Button(root, text="Bom dia", command=lambda: atualizar_texto("Bom dia")).pack()
tk.Button(root, text="Boa tarde", command=lambda: atualizar_texto("Boa tarde")).pack()
tk.Button(root, text="Boa noite", command=lambda: atualizar_texto("Boa noite")).pack()

root.mainloop()