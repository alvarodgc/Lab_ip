import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("400x300")

texto = tk.Label(ventana, text="Hola mundo cruel")
texto.pack(pady=50)

boton = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
boton.pack()

ventana.mainloop()