# Definição da classe ListNode (fornecida pelo LeetCode)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Soma dois números representados por listas encadeadas.

        Args:
            l1: Primeira lista encadeada representando um número
            l2: Segunda lista encadeada representando um número
        
        Returns:
            Lista encadeada representando a soma dos dois números
        '''

        # Nó dummy (fictício) para facilitar a construção da lista resultado
        # Isso evita tratamento especial para o primeira nó
        dummy_head = ListNode()

        # Variável para armazenar o "vai-um" da adição
        carry = 0

        # Ponteiro atual que percorre a lista resultado
        current = dummy_head

        # Loop enquanto houver nós em l1, l2 e carry pendente
        while l1 or l2 or carry:
            # Obtém o valor do nó atual de l1 (0 se a lista acabou)
            val1 = l1.val if l1 else 0

            # Obtem o valor do nó l2 (0 se a lista acabou)
            val2 = l2.val if l2 else 0

            # Calcula a soma: digito1 + dígito2 + carry anterior
            total = val1 + val2 + carry

            # Calcula o novo carry (divisão inteira por 10)
            # e o dígito a ser armazenado (resto da divisão por 10)
            carry = total // 10
            digit = total % 10

            # Cria um novo nó com o dígito calculado
            current.next = ListNode(digit)

            # Avança o ponteiro current
            current = current.next

            # Avança para o próximo nó de l1, se existir
            l1 = l1.next if l1 else None

            # Avança para o próximo nó de l2, se existir
            l2 = l2.next if l2 else None
        
        # Retorna o resultado (pula o nó dummy)
        return dummy_head.next
    
# ========== CÓDIGO DE TESTE ==========

def criar_lista(numeros):
    """
    Função auxiliar para criar uma lista encadeada a partir de uma lista Pyhton
    Exemplo: [2,4,3] vira 2 -> 4 -> 3
    """

    dummy = ListNode()
    current = dummy

    for num in numeros:
        current.next = ListNode(num)
        current = current.next
    
    return dummy.next

def mostrar_lista(node):
    """
    Função auxiliar para mostrar a lista encadeada de forma legível.
    """

    valores = []
    while node:
        valores.append(str(node.val))
        node = node.next

    return " -> ".join(valores)

# TESTANDO A SOLUÇÃO
if __name__ == "__main__":
    # Criar instâncias da solução
    sol = Solution()

    # Teste 1: 342 + 465 = 807
    # l1 = [2,4,3] representa 342
    # l2 = [5,6,4] representa 465
    print("=== Teste 1 ===")
    l1 = criar_lista([2,4,3])
    l2 = criar_lista([5,6,4])
    resultado = sol.addTwoNumbers(l1, l2)
    print(f"Input: l1 = [2,4,3], l2 = [5,6,4]")
    print(f"Output: [{mostrar_lista(resultado)}]")
    print(f"Explicação: 342 + 465 = 807\n")

    # Teste 2: 0 + 0 = 0
    print("=== Teste 2 ===")
    l1 = criar_lista([0])
    l2 = criar_lista([0])
    resultado = sol.addTwoNumbers(l1, l2)
    print(f"Input: l1 = [0], l2 = [0]")
    print(f"Output: [{mostrar_lista(resultado)}]")
    print(f"Explicação: 0 + 0 = 0\n")

    # Teste 3: 9999999 + 9999 = 10009998
    print("=== Teste 3 ===")
    l1 = criar_lista([9,9,9,9,9,9,9])
    l2 = criar_lista([9,9,9,9])
    resultado = sol.addTwoNumbers(l1, l2)
    print(f"Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]")
    print(f"Output: [{mostrar_lista(resultado)}]")
    print(f"Explicação: 9999999 + 9999 = 10009998")