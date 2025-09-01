import tkinter as tk

root = tk.Tk()
root.title("Texto Personalizado")

label = tk.Label(root, text="Texto Personalizado", font=("Arial", 20), fg="blue")
label.pack()

root.mainloop()