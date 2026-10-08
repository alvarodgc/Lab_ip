import tkinter as tk

# ==============================
# CONFIGURACIÓN
# ==============================

TAMAÑO_LETRA = 20
COLOR_LETRA = "blue"
COLOR_FONDO = "black"

ANCHO = 500
ALTO = 300

# ==============================
# VENTANA
# ==============================

ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry(f"{ANCHO}x{ALTO}")
ventana.configure(bg=COLOR_FONDO)

# Texto
texto = tk.Label(
    ventana,
    text="Hola mundo cruel, porque el pais necesita mas ingenieros de software",
    font=("Arial", TAMAÑO_LETRA),
    fg=COLOR_LETRA,
    bg=COLOR_FONDO
)

texto.pack(expand=True)

# Botón
boton = tk.Button(
    ventana,
    text="Cerrar",
    command=ventana.destroy
)

boton.pack(pady=10)

# Iniciar
ventana.mainloop()  # la función mainloop() mantiene la ventana abierta y en espera de eventos