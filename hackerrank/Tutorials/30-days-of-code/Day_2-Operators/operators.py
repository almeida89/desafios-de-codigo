import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    # Calcula o valor da gorjeta com base na porcentagem informada
    tip = meal_cost * tip_percent / 100
    # Calcula o valor do imposto com base na porcentagem informada
    tax = meal_cost * tax_percent / 100
    # Soma o custo da refeição, gorjeta e imposto para obter o custo total
    total_cost = meal_cost + tip + tax
    # Imprime o resultado arredondando para o inteiro mais próximo
    print(round(total_cost))
    

if __name__ == '__main__':
    # Lê o custo da refeição (float)
    meal_cost = float(input().strip())
    # Lê a porcentagem da gorjeta (int)
    tip_percent = int(input().strip())
    # Lê a porcentagem do imposto (int)
    tax_percent = int(input().strip())
    # Chama a função para calcular e imprimir o custo total
    solve(meal_cost, tip_percent, tax_percent)