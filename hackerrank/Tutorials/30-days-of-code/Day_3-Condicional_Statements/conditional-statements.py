import math
import os
import random
import re
import sys

def solve_weirdness(n):
    '''
    Analisa um inteiro e retorna 'Weird' ou 'Not Weird' baseado em um conjunto de regras
    '''

    # 1. Checagem primária: Impar ou Par?
    # Usamos o operador de módulo (%) para verificar o resto da divisão por 2.
    if n % 2 != 0:
        # Se o resto não for 0, o número é impar.
        # Esta é a regra mais simples e cobre metade dos casos.
        return "Weird"
    else:
        # 2. Lógica aninhada: O número é par.
        # Agora, tratamos as regras específicadas para números pares.

        if n in range(2, 6): # Intervalo inclusivo [2, 5]
            return "Not Weird"
        elif n in range(6, 21): # Intervalo inclusivo [6, 20]
            return "Weird"
        elif n > 20:
            return "Not Weird"
        
if __name__ == '__main__':
    # Esta é a entrada padrão (stub) fornecida pelo desafio.
    try:
        n = int(input().strip())

        # Chamamos nossa função de lógica de negócios
        result = solve_weirdness(n)

        # Imprimimos o resultado
        print(result)

    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        