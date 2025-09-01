import tkinter as tk

def salvar():
    compromisso = entrada.get()
    if compromisso:
        lista.insert(tk.END, compromisso)
        entrada.delete(0, tk.END)

root = tk.Tk()
root.title("Mini Agenda")

entrada = tk.Entry(root)
entrada.pack()

tk.Button(root, text="Salvar", command=salvar).pack()

lista = tk.Listbox(root)
lista.pack()

root.mainloop()