# Valores y sus grados de pertenencia
valores = [10, 20, 30]
grados = [0.2, 0.5, 0.8]

# Fórmula del centroide: (Σ μ(x) * x) / (Σ μ(x))
numerador = sum(mu * x for mu, x in zip(grados, valores))
denominador = sum(grados)
centroide = numerador / denominador

print("Valores:", valores)
print("Grados de pertenencia:", grados)
print(f"Valor defuzificado (centroide): {centroide:.2f}")