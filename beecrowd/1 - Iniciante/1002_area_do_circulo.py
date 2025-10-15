# Define o valor da constante pi para o cálculo da área
n = 3.14159

# Lê o valor do raio da circunferência como número de ponto flutuante
raio = float(input())

# Calcula a área da circunferência usando a fórmula: área = pi * raio^2
area = n * (raio ** 2)

# Imprime o resultado formatado com 4 casas decimais
# A string f-string já adiciona a quebra de linha automaticamente
print(f"A={area:.4f}")