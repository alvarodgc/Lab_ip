
import tkinter as tk
from tkinter import messagebox


# ---------------------------------------------------------
# FUNCIÓN: calcular
# Descripción: Obtiene los datos, valida la información
# y realiza la operación seleccionada.
# ---------------------------------------------------------
def calcular():
    try:
        # Obtener los números de las cajas de texto
        a = float(entrada_numero1.get())
        b = float(entrada_numero2.get())

    except ValueError:
        # Se muestra si el usuario introduce algo que no sea número
        messagebox.showerror(
            "Error",
            "Por favor, ingrese valores numéricos válidos."
        )
        return

    # Verificar que se haya seleccionado una operación
    operacion = operacion_seleccionada.get()

    if operacion == "":
        messagebox.showerror(
            "Error",
            "Por favor, seleccione una operación."
        )
        return

    # Realizar la operación seleccionada
    if operacion == "+":
        resultado = a + b

    elif operacion == "-":
        resultado = a - b

    elif operacion == "*":
        resultado = a * b

    elif operacion == "/":
        # Verificar que no se intente dividir entre cero
        if b == 0:
            messagebox.showerror(
                "Error",
                "No se puede dividir entre cero."
            )
            return

        resultado = a / b

    # Mostrar el resultado en la caja correspondiente
    caja_resultado.config(state="normal")
    caja_resultado.delete(0, tk.END)
    caja_resultado.insert(0, str(resultado))
    caja_resultado.config(state="readonly")


# ---------------------------------------------------------
# FUNCIÓN: limpiar
# Descripción: Borra los datos de las cajas y
# deselecciona la operación.
# ---------------------------------------------------------
def limpiar():
    entrada_numero1.delete(0, tk.END)
    entrada_numero2.delete(0, tk.END)

    operacion_seleccionada.set("")

    caja_resultado.config(state="normal")
    caja_resultado.delete(0, tk.END)
    caja_resultado.config(state="readonly")


# ---------------------------------------------------------
# FUNCIÓN: salir
# Descripción: Cierra la ventana del programa.
# ---------------------------------------------------------
def salir():
    ventana.destroy()


# ---------------------------------------------------------
# VENTANA PRINCIPAL
# ---------------------------------------------------------

ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("400x400")
ventana.resizable(False, False)


# ---------------------------------------------------------
# TÍTULO
# ---------------------------------------------------------

titulo = tk.Label(
    ventana,
    text="CALCULADORA BÁSICA",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)


# ---------------------------------------------------------
# PRIMER NÚMERO
# ---------------------------------------------------------

tk.Label(
    ventana,
    text="Primer número:"
).pack()

entrada_numero1 = tk.Entry(
    ventana,
    width=30
)
entrada_numero1.pack(pady=5)


# ---------------------------------------------------------
# SEGUNDO NÚMERO
# ---------------------------------------------------------

tk.Label(
    ventana,
    text="Segundo número:"
).pack()

entrada_numero2 = tk.Entry(
    ventana,
    width=30
)
entrada_numero2.pack(pady=5)


# ---------------------------------------------------------
# OPERACIONES
# Los Radiobutton están agrupados mediante la variable
# operacion_seleccionada.
# ---------------------------------------------------------

tk.Label(
    ventana,
    text="Seleccione una operación:"
).pack(pady=10)

operacion_seleccionada = tk.StringVar()
operacion_seleccionada.set("")

frame_operaciones = tk.Frame(ventana)
frame_operaciones.pack()

tk.Radiobutton(
    frame_operaciones,
    text="Suma (+)",
    variable=operacion_seleccionada,
    value="+"
).grid(row=0, column=0, padx=5)

tk.Radiobutton(
    frame_operaciones,
    text="Resta (-)",
    variable=operacion_seleccionada,
    value="-"
).grid(row=0, column=1, padx=5)

tk.Radiobutton(
    frame_operaciones,
    text="Multiplicación (*)",
    variable=operacion_seleccionada,
    value="*"
).grid(row=0, column=2, padx=5)

tk.Radiobutton(
    frame_operaciones,
    text="División (/)",
    variable=operacion_seleccionada,
    value="/"
).grid(row=0, column=3, padx=5)


# ---------------------------------------------------------
# RESULTADO
# ---------------------------------------------------------

tk.Label(
    ventana,
    text="Resultado:"
).pack(pady=10)

caja_resultado = tk.Entry(
    ventana,
    width=30,
    state="readonly"
)
caja_resultado.pack(pady=5)


# ---------------------------------------------------------
# BOTONES
# ---------------------------------------------------------

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

tk.Button(
    frame_botones,
    text="Calcular",
    width=10,
    command=calcular
).grid(row=0, column=0, padx=5)

tk.Button(
    frame_botones,
    text="Limpiar",
    width=10,
    command=limpiar
).grid(row=0, column=1, padx=5)

tk.Button(
    frame_botones,
    text="Salir",
    width=10,
    command=salir
).grid(row=0, column=2, padx=5)


# ---------------------------------------------------------
# INICIAR EL PROGRAMA
# ---------------------------------------------------------

ventana.mainloop()

