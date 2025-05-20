# questao3.py
import json

# Suponha que você tenha um arquivo faturamento.json
with open('faturamento.json') as f:
    dados = json.load(f)

valores = [v for v in dados if v > 0]
media = sum(valores) / len(valores)

print(f"Menor faturamento: {min(valores)}")
print(f"Maior faturamento: {max(valores)}")
print(f"Dias com faturamento acima da média: {sum(1 for v in valores if v > media)}")
