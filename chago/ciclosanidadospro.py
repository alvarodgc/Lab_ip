import tkinter as tk
from tkinter import messagebox


# ---------------------------------------------------------
# FUNCIÓN PARA CALCULAR LAS TABLAS
# ---------------------------------------------------------
def calcular():
    try:
        # Obtener los valores de las cajas de texto
        inicio_exterior = int(txt_inicio_tabla.get())
        fin_exterior = int(txt_fin_tabla.get())

        inicio_interior = int(txt_inicio_mult.get())
        fin_interior = int(txt_fin_mult.get())

        # Validar que los inicios no sean mayores que los finales
        if inicio_exterior > fin_exterior:
            messagebox.showerror(
                "Error",
                "El inicio de la tabla no puede ser mayor que el final."
            )
            return

        if inicio_interior > fin_interior:
            messagebox.showerror(
                "Error",
                "El inicio de la multiplicación no puede ser mayor que el final."
            )
            return

        # Limpiar resultados anteriores
        lista_resultados.delete(0, tk.END)

        # Ciclo exterior
        i = inicio_exterior

        while i <= fin_exterior:

            lista_resultados.insert(
                tk.END,
                "Tabla = " + str(i)
            )

            # Ciclo interior
            j = inicio_interior

            while j <= fin_interior:

                resultado = i * j

                lista_resultados.insert(
                    tk.END,
                    str(i) + " * " + str(j) + " = " + str(resultado)
                )

                j = j + 1

            # Espacio entre tablas
            lista_resultados.insert(tk.END, "")

            i = i + 1

    except ValueError:
        messagebox.showerror(
            "Error",
            "Por favor, introduce solamente números enteros."
        )


# ---------------------------------------------------------
# FUNCIÓN PARA LIMPIAR
# ---------------------------------------------------------
def limpiar():

    txt_inicio_tabla.delete(0, tk.END)
    txt_fin_tabla.delete(0, tk.END)

    txt_inicio_mult.delete(0, tk.END)
    txt_fin_mult.delete(0, tk.END)

    lista_resultados.delete(0, tk.END)

    # Colocar valores iniciales
    txt_inicio_tabla.insert(0, "1")
    txt_fin_tabla.insert(0, "10")

    txt_inicio_mult.insert(0, "1")
    txt_fin_mult.insert(0, "10")


# ---------------------------------------------------------
# FUNCIÓN PARA SALIR
# ---------------------------------------------------------
def salir():
    respuesta = messagebox.askyesno(
        "Salir",
        "¿Deseas salir del programa?"
    )

    if respuesta:
        ventana.destroy()


# ---------------------------------------------------------
# VENTANA PRINCIPAL
# ---------------------------------------------------------

ventana = tk.Tk()

ventana.title("Tablas de Multiplicar")
ventana.geometry("750x600")
ventana.resizable(False, False)

# ---------------------------------------------------------
# TÍTULO
# ---------------------------------------------------------

titulo = tk.Label(
    ventana,
    text="Tablas de Multiplicar",
    font=("Arial", 20, "bold")
)

titulo.pack(pady=15)


# ---------------------------------------------------------
# MARCO PRINCIPAL
# ---------------------------------------------------------

marco = tk.Frame(ventana)
marco.pack(padx=20, pady=5)


# ---------------------------------------------------------
# SECCIÓN DE DATOS
# ---------------------------------------------------------

marco_datos = tk.LabelFrame(
    marco,
    text="Datos de las tablas",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=15
)

marco_datos.grid(row=0, column=0, padx=10, pady=10, sticky="n")


# Inicio de tabla
lbl_inicio_tabla = tk.Label(
    marco_datos,
    text="Tabla inicial:"
)

lbl_inicio_tabla.grid(
    row=0,
    column=0,
    padx=5,
    pady=8,
    sticky="w"
)

txt_inicio_tabla = tk.Entry(
    marco_datos,
    width=15
)

txt_inicio_tabla.grid(
    row=0,
    column=1,
    padx=5,
    pady=8
)


# Fin de tabla
lbl_fin_tabla = tk.Label(
    marco_datos,
    text="Tabla final:"
)

lbl_fin_tabla.grid(
    row=1,
    column=0,
    padx=5,
    pady=8,
    sticky="w"
)

txt_fin_tabla = tk.Entry(
    marco_datos,
    width=15
)

txt_fin_tabla.grid(
    row=1,
    column=1,
    padx=5,
    pady=8
)


# Inicio de multiplicación
lbl_inicio_mult = tk.Label(
    marco_datos,
    text="Inicio de mult.:"
)

lbl_inicio_mult.grid(
    row=2,
    column=0,
    padx=5,
    pady=8,
    sticky="w"
)

txt_inicio_mult = tk.Entry(
    marco_datos,
    width=15
)

txt_inicio_mult.grid(
    row=2,
    column=1,
    padx=5,
    pady=8
)


# Fin de multiplicación
lbl_fin_mult = tk.Label(
    marco_datos,
    text="Final de mult.:"
)

lbl_fin_mult.grid(
    row=3,
    column=0,
    padx=5,
    pady=8,
    sticky="w"
)

txt_fin_mult = tk.Entry(
    marco_datos,
    width=15
)

txt_fin_mult.grid(
    row=3,
    column=1,
    padx=5,
    pady=8
)


# ---------------------------------------------------------
# SECCIÓN DE RESULTADOS
# ---------------------------------------------------------

marco_resultados = tk.LabelFrame(
    marco,
    text="Resultados",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)

marco_resultados.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)


# Lista donde aparecen las tablas
lista_resultados = tk.Listbox(
    marco_resultados,
    width=35,
    height=18,
    font=("Courier New", 11)
)

lista_resultados.grid(
    row=0,
    column=0,
    sticky="nsew"
)


# Barra de desplazamiento
scroll = tk.Scrollbar(
    marco_resultados,
    orient=tk.VERTICAL,
    command=lista_resultados.yview
)

scroll.grid(
    row=0,
    column=1,
    sticky="ns"
)

lista_resultados.config(
    yscrollcommand=scroll.set
)


# ---------------------------------------------------------
# BOTONES
# ---------------------------------------------------------

marco_botones = tk.Frame(ventana)

marco_botones.pack(
    pady=20
)


# Botón Limpiar
btn_limpiar = tk.Button(
    marco_botones,
    text="Limpiar",
    width=12,
    font=("Arial", 11, "bold"),
    command=limpiar
)

btn_limpiar.grid(
    row=0,
    column=0,
    padx=10
)


# Botón Calcular
btn_calcular = tk.Button(
    marco_botones,
    text="Calcular",
    width=12,
    font=("Arial", 11, "bold"),
    command=calcular
)

btn_calcular.grid(
    row=0,
    column=1,
    padx=10
)


# Botón Salir
btn_salir = tk.Button(
    marco_botones,
    text="Salir",
    width=12,
    font=("Arial", 11, "bold"),
    bg="red",
    fg="white",
    activebackground="darkred",
    activeforeground="white",
    command=salir
)

btn_salir.grid(
    row=0,
    column=2,
    padx=10
)


# ---------------------------------------------------------
# VALORES INICIALES
# ---------------------------------------------------------

txt_inicio_tabla.insert(0, "1")
txt_fin_tabla.insert(0, "10")

txt_inicio_mult.insert(0, "1")
txt_fin_mult.insert(0, "10")


# ---------------------------------------------------------
# INICIAR PROGRAMA
# ---------------------------------------------------------

ventana.mainloop()