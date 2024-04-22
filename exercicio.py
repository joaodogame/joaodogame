v1 = float(input())
v2 = float(input())
v3 = float(input())
valores_iguais = 0

# Verifica se v1 é igual a v2 ou v3
if v1 == v2 or v1 == v3:
    valores_iguais += 1

# Verifica se v2 é igual a v3 (sem repetir a verificação de v1)
if v2 == v3:
    valores_iguais += 1

print(valores_iguais)