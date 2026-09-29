MAX = 3

for intento in range(1, MAX + 1):
    usuario = input("Usuario: ").strip().lower()
    clave = input("Contraseña: ").strip()        #el strip() elimina los espacios en blanco al inicio y al final de la cadena

    if usuario == "alumno" and clave == "python123":
        print("Bienvenido")
        break

    print("Credenciales incorrectas")
else:
    print("Acceso bloqueado")
       