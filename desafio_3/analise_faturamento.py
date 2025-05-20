# questao3.py
import json

with open('desafio_3/faturamento.json') as f:
    dados = json.load(f)

valores = [v for v in dados if v > 0]
media = sum(valores) / len(valores)

print(f"Menor faturamento: R${min(valores):.2f}")
print(f"Maior faturamento: R${max(valores):.2f}")
print(f"Dias com faturamento acima da média: {sum(1 for v in valores if v > media)}")
