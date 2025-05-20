# questao2.py
def fibonacci(n):
    seq = [0, 1]
    while seq[-1] < n:
        seq.append(seq[-1] + seq[-2])
    return seq if seq[-1] == n else seq[:-1]

def pertence_a_fibonacci(n):
    seq = fibonacci(n)
    if n in seq:
        return f"O número {n} pertence à sequência de Fibonacci!"
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

numero = int(input("Digite um número: "))
print(pertence_a_fibonacci(numero))
