import tkinter as tk

def calcular():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.config(text=f"Soma: {n1 + n2}")
    except ValueError:
        resultado.config(text="Digite números válidos.")

root = tk.Tk()
root.title("Calculadora Simples")
root.geometry("300x150")

tk.Label(root, text="Número 1:").pack()
entrada1 = tk.Entry(root)
entrada1.pack()

tk.Label(root, text="Número 2:").pack()
entrada2 = tk.Entry(root)
entrada2.pack()

tk.Button(root, text="Calcular", command=calcular).pack(pady=10)

resultado = tk.Label(root, text="")
resultado.pack()

root.mainloop()

