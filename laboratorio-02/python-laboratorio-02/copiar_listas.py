original = ["Teclado", "Mouse"]
otra_referencia = original

otra_referencia.append("Monitor")
print(original)  # También cambió: ambas variables apuntan a la misma lista

print()
original = ["Teclado", "Mouse"]
copia = original.copy()

copia.append("Monitor")
print("Original:", original)
print("Copia:", copia)
