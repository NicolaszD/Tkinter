import tkinter as tk

def verificar():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == "admin" and senha == "123":
        resultado.config(text="Acesso permitido")
    else:
        resultado.config(text="Acesso negado")

root = tk.Tk()
root.title("Login Simples")

tk.Label(root, text="Usuário:").pack()
entrada_usuario = tk.Entry(root)
entrada_usuario.pack()

tk.Label(root, text="Senha:").pack()
entrada_senha = tk.Entry(root, show="*")
entrada_senha.pack()

tk.Button(root, text="Entrar", command=verificar).pack()

resultado = tk.Label(root, text="")
resultado.pack()

root.mainloop()