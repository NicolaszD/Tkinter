import tkinter as tk 


root = tk.Tk()
root.title("Aplicativo Hello World")  


label = tk.Label(root, text="Minha Primeira Janela")
label.pack()
root.geometry("400x300")

root.mainloop()