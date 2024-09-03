import json
with open('/mnt/data/dados.json', 'r') as file:
    dados = json.load(file)


fat_diario = [dia['valor'] for dia in dados if dia['valor'] > 0]


menor_fat = min(fat_diario)
maior_fat = max(fat_diario)


media_mensal = sum(fat_diario) / len(fat_diario)


dias_acima_da_media = len([valor for valor in fat_diario if valor > media_mensal])


print(f"Menor valor de faturamento: {menor_fat:.2f}")
print(f"Maior valor de faturamento: {maior_fat:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")