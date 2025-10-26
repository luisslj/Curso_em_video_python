# Definindo os parâmetros da PA
primeiro_termo = 2
razao = 3
n = 10  # número de termos

# Gerando e exibindo os termos
print("Progressão Aritmética:")
soma = 0
for i in range(n):
    termo = primeiro_termo + i * razao
    print(f"Termo {i+1}: {termo}")
    soma += termo

# Exibindo a soma dos termos
print(f"\nSoma dos {n} primeiros termos: {soma}")