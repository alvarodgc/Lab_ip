Usuario = "alumno"
Clave = "python123"

usuario= input("Usuario: ").strip().lower()
clave= input("Clave: ").strip()

if usuario == Usuario and clave == Clave:
    print("Bienbenido")
else:
    print("Credenciales incorrectas")