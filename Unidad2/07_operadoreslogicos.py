edad=19
tiene_credencial=True
tien_adeudo=True

es_mayor=edad >= 18
documento_valido=tiene_credencial
sin_adeudo=not tien_adeudo

autorizado=es_mayor or documento_valido and sin_adeudo
print(autorizado)
