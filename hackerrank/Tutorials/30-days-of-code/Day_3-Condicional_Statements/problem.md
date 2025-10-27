# Intuição

Minha intuição imediata ao ler este problema é que se trata se um exercício clássico de "mapeamento de condições para resultados". O problema nos dá um conjunto de regras de negócios (as condições) e um conjunto de saídas ("Weird", "Not Weird").

A estrutura de dados mais fundamental para lidar com regras de negócios excludentes é uma árvire de decisão, que em programaçao é implementada diretamente com as declarações `if`, `elif` e `else`.

A intuição principal é notal que as regras são hierárquicas. A "grande divisão" ( o primeiro nó da nossa árvore de decisão) e entre **impar** e **par**. Se o número for impar, o jogo é (é "Weird"). Se for par, um novo conjunto de sub-regras se aplica. Isso me diz que a primeira coisa que meu código deve fazer é checar a paridade.

# A Estratégia

Baseado na intuição, a estratégia é construir uma árvore de decisão lógica que espelhe as regras da forma mais limpa e eficiente possível.

1. **Entrada**: Receber o número `n`.

2. **Decisão Primária(Raiz)**: Verificar a paridade de `n`. A ferramente mais eficiente para isso é o operador de módulo (`%`).
* `if n % 2 != 0:` (Se o resto da divisão por 2 for divergente de 0, é ímpar).

3. **Ramo 1 (impar)**: Se a condição acima for `True`, a regra é única:
* Retorne ou imprima "Weird".
* A execução lógica para este ramo termina aqui.

4. **Ramo 2 (Par)**: Se a condição primária for `False`, o número é garantidamente par. Usamos um `else` para capturar este "contexto".

5. **Decisões Secundárias (Aninhadas)**: Agora, dentro do bloco `else`, precisamos lidar com as três sub-regras para números pares. Usamos uma nova cadeia `if/elif/else` aninhada.
* **Sub-regra A**: `if n in range(2, 6):` (Isso cobre o intervalo inclusivo de 2 a 5).
    * Retorne ou imprima "Not Weird".
* **Sub-regra B**: `elif n in range(6, 21):` (Isso cobre o intervalo inclusivo de 6 a 20).
    * Retorne ou imprima "Weird".
* **Sub-regra C**: `else:` (Esta é a captura-geral. Se é par e não se encaixa nas regras A ou B, só pode ser `n > 20`).
    * Retorne ou imprima "Not Weird".

Essa abordagem aninhada é superior a uma abordagem "plana" (com `and`), pois é mais eficiente (não checmaos `n % 2 == 0` múltiplas vezes) e mais legível, pois o aninhamento fornece contexto (já sabemos que o número é par dentro daquele bloco).