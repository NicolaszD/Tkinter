import tkinter as tk

root = tk.Tk()
root.title("Sair da Aplicação")

tk.Button(root, text="Sair", command=root.destroy).pack()

root.mainloop()