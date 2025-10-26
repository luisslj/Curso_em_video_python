# Base de dados simples
frases = [
    "eu amo este lugar",
    "isso é horrível",
    "estou muito feliz",
    "que dia terrível",
    "isso é maravilhoso",
    "não gostei disso"
]

# Rótulos: 1 = positivo, 0 = negativo
rotulos = [1, 0, 1, 0, 1, 0]

# Palavras positivas e negativas conhecidas
positivas = ["amo", "feliz", "maravilhoso"]
negativas = ["horrível", "terrível", "não", "gostei"]

# Função para extrair características
def extrair_caracteristicas(frase):
    palavras = frase.lower().split()
    score = 0
    for palavra in palavras:
        if palavra in positivas:
            score += 1
        elif palavra in negativas:
            score -= 1
    return score

# Treinamento (ajuste de limiar)
limiar = 0  # valor inicial
for i in range(len(frases)):
    score = extrair_caracteristicas(frases[i])
    if rotulos[i] == 1 and score <= limiar:
        limiar -= 1
    elif rotulos[i] == 0 and score > limiar:
        limiar += 1

# Teste
nova_frase = "não gostei desse lugar"
score = extrair_caracteristicas(nova_frase)
resultado = 1 if score > limiar else 0
print("Sentimento:", "Positivo" if resultado == 1 else "Negativo")