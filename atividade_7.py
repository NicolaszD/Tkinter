import tkinter as tk

def mudar_cor(cor):
    root.configure(bg=cor)

root = tk.Tk()
root.title("Mudar Cor de Fundo")
root.geometry("300x200")

tk.Button(root, text="Vermelho", command=lambda: mudar_cor("red")).pack()
tk.Button(root, text="Verde", command=lambda: mudar_cor("green")).pack()
tk.Button(root, text="Azul", command=lambda: mudar_cor("blue")).pack()

root.mainloop()
