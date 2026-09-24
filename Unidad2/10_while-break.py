while True:
    opcion = input("Elige A, B o C: ").strip().upper()   #uper sirve para convertir a mayusculas y strip para quitar espacios

    if opcion in ("A", "B", "C"):
        break
    print("Opción inválida. Intenta de nuevo.")
print(f"Elegiste {opcion}")              