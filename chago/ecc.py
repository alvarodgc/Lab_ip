import tkinter as tk
from math import sqrt, fabs

# ------------------- VENTANA PRINCIPAL -------------------
ventana = tk.Tk()
ventana.title("Ecuación Cuadrática | Solucionador")
ventana.geometry("580x540")
ventana.resizable(False, False)
ventana.config(bg="#e8eff7")

# ------------------- FUENTES Y COLORES -------------------
fuente_titulo = ("Segoe UI", 16, "bold")
fuente_ecuacion = ("Segoe UI", 20, "bold")
fuente_entrada = ("Segoe UI", 16, "bold")
fuente_boton = ("Segoe UI", 11, "bold")
fuente_resultado = ("Segoe UI", 12)

color_fondo = "#e8eff7"
color_marco = "#ffffff"
color_texto = "#1a365d"
color_calcular = "#2563eb"
color_limpiar = "#f59e0b"
color_salir = "#dc2626"
color_caja = "#f0f4f9"

# ------------------- TÍTULO -------------------
tk.Label(ventana,
         text="Solución de una Ecuación Cuadrática",
         font=fuente_titulo,
         bg=color_fondo,
         fg=color_texto).pack(pady=18)

# ------------------- MARCO PRINCIPAL -------------------
marco = tk.Frame(ventana, bg=color_marco, bd=3, relief="ridge", padx=25, pady=25)
marco.pack(padx=25, pady=5, fill="both", expand=True)

# ------------------- ECUACIÓN -------------------
marco_eq = tk.Frame(marco, bg=color_marco)
marco_eq.pack(pady=10)

estilo_ent = {"font": fuente_entrada, "width": 4, "justify": "center",
              "bd": 2, "relief": "solid", "bg": "#f8fbff", "fg": color_texto}

entry_a = tk.Entry(marco_eq, **estilo_ent)
entry_a.grid(row=0, column=0, padx=5)
tk.Label(marco_eq, text="x² +", font=fuente_ecuacion, bg=color_marco, fg=color_texto).grid(row=0, column=1)

entry_b = tk.Entry(marco_eq, **estilo_ent)
entry_b.grid(row=0, column=2, padx=5)
tk.Label(marco_eq, text="x +", font=fuente_ecuacion, bg=color_marco, fg=color_texto).grid(row=0, column=3)

entry_c = tk.Entry(marco_eq, **estilo_ent)
entry_c.grid(row=0, column=4, padx=5)
tk.Label(marco_eq, text="c = 0", font=fuente_ecuacion, bg=color_marco, fg=color_texto).grid(row=0, column=5)

# ------------------- CAJA DE RESULTADOS -------------------
resultado = tk.Label(marco, text="", font=fuente_resultado, bg=color_caja,
                     fg=color_texto, width=52, height=13, relief="solid", bd=2,
                     justify="left", anchor="nw", padx=15, pady=15)
resultado.pack(pady=15)

# ------------------- FUNCIÓN DE CÁLCULO (CORREGIDA) -------------------
def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            resultado.config(text="⚠️  'a' no puede ser 0\nNo es ecuación cuadrática.")
            return

        d = b**2 - 4*a*c

        # Siempre calculamos parte real e imaginaria para AMBAS raíces
        if d > 0:
            tipo = "✅ Raíces Reales Distintas"
            r1_real = (-b + sqrt(d)) / (2*a)
            r1_imag = 0.0
            r2_real = (-b - sqrt(d)) / (2*a)
            r2_imag = 0.0

        elif d == 0:
            tipo = "✅ Raíz Real Doble"
            r1_real = -b / (2*a)
            r1_imag = 0.0
            r2_real = r1_real
            r2_imag = 0.0

        else:
            tipo = "⚠️ Raíces Complejas/Imaginarias"
            r1_real = -b / (2*a)
            r1_imag = sqrt(fabs(d)) / (2*a)
            r2_real = r1_real
            r2_imag = -r1_imag

        # Mostramos SIEMPRE ambas partes
        res = f"{tipo}\n\n"
        res += "─── Raíz 1 ───\n"
        res += f"Parte Real:      {r1_real:.6f}\n"
        res += f"Parte Imaginaria: {r1_imag:.6f}\n"
        res += f"Forma completa:  {r1_real:.6f} + {r1_imag:.6f}i\n\n"
        res += "─── Raíz 2 ───\n"
        res += f"Parte Real:      {r2_real:.6f}\n"
        res += f"Parte Imaginaria: {abs(r2_imag):.6f}\n"
        signo = "+" if r2_imag >= 0 else "-"
        res += f"Forma completa:  {r2_real:.6f} {signo} {abs(r2_imag):.6f}i"

        resultado.config(text=res)

    except ValueError:
        resultado.config(text="❌ Escribe solo números en las casillas")

def limpiar():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    resultado.config(text="")
    entry_a.focus()

def salir():
    ventana.destroy()

# ------------------- BOTONES -------------------
marco_btn = tk.Frame(marco, bg=color_marco)
marco_btn.pack(pady=5)

estilo_btn = {"font": fuente_boton, "width": 13, "relief": "flat", "pady": 8, "cursor": "hand2"}

tk.Button(marco_btn, text="Calcular", command=calcular,
          bg=color_calcular, fg="white", **estilo_btn).grid(row=0, column=0, padx=8)

tk.Button(marco_btn, text="Limpiar", command=limpiar,
          bg=color_limpiar, fg="#1f2937", **estilo_btn).grid(row=0, column=1, padx=8)

tk.Button(marco_btn, text="Salir", command=salir,
          bg=color_salir, fg="white", **estilo_btn).grid(row=0, column=2, padx=8)

ventana.mainloop()