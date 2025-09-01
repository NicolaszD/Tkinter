import tkinter as tk

def contar():
    def atualizar():
        nonlocal tempo
        if tempo >= 0:
            label.config(text=str(tempo))
            tempo -= 1
            root.after(1000, atualizar)

    tempo = 10
    atualizar()

root = tk.Tk()
root.title("Contador Regressivo")

label = tk.Label(root, text="10", font=("Arial", 24))
label.pack()

tk.Button(root, text="Iniciar", command=contar).pack()

root.mainloop()
