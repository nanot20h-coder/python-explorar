nombre_trabajador = "Sara"
horas_trabajadas = 36
valor_hora = 20000.0

pago_total = horas_trabajadas * valor_hora

APORTE = 0.04
valor_aporte = pago_total * APORTE

print("-------------------------")
print("RESUMEN DE PAGO")
print("-------------------------")
print("Trabajador:", nombre_trabajador)
print("Horas:", horas_trabajadas)
print("Valor por hora: $", valor_hora)
print("Pago total: $", pago_total)
print("Aporte 4%: $", valor_aporte)