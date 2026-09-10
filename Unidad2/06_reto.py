total_cuenta = float(input("Total de la cuenta: "))
porcentaje_propina = float(input("Porcentaje de propina: "))
numero_personas = int(input("Numero de personas: "))
Propina = total_cuenta * (porcentaje_propina / 100)
Total_con_propina = total_cuenta + Propina
Total_por_persona = Total_con_propina / numero_personas
print(f"Propina: {Propina:.2f}") 
print(f"Total con propina: {Total_con_propina:.2f}")
print(f"Total por persona: {Total_por_persona:.2f}")
