faturas = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = 0

for cidade in faturas:
    total += faturas[cidade]

porcentagem = 0

for cidade in faturas:
    porcentagem = faturas[cidade] * 100 / total
    print(f"Percentual de {cidade}: {porcentagem:.2f}%")
