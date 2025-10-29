# 🧩 02 - Add Two Sum

## 💡 Ideia Inicial

Quando vi esse problema pela primeira vez, lembrei de como faço soma no papel: começo pelos dígitos da direita e vou somando um por um, levando o "vai-um" quando a soma passa de 9.  
A grande sacada aqui é que os números já estão de trás para frente na lista encadeada — então não preciso reverter nada!  
Posso simplesmente percorrer as duas listas ao mesmo tempo, somando os valores e cuidando do "vai-um" (*carry*).

---

## ⚙️ Abordagem

Minha abordagem foi simples e direta.  
Criei um nó “dummy” (fictício) para facilitar a construção da lista resultado — assim não preciso me preocupar com casos especiais no começo.

Depois, fiz um loop que percorre as duas listas simultaneamente.  
Em cada passo, pego o valor de cada nó (ou zero se a lista já acabou), somo esses valores junto com o *carry* da iteração anterior.  

O resultado dessa soma me dá dois números importantes:
- O dígito que vou guardar (usando o resto da divisão por 10);  
- O novo *carry* (usando a divisão inteira por 10).  

Crio um novo nó com esse dígito e avanço para os próximos nós das listas.  
Continuo fazendo isso até que ambas as listas acabem — e não haja mais *carry* pendente.

---

## 🧮 Resultado

<p align="center">
  <img src="https://github.com/almeida89/desafios-de-codigo/blob/main/leetcode/02_Add_Two_Numbers/img/addtwonumbers.png" alt="Saída do código" width="600"/>
</p>

<p align="center">
  <em>Saída gerada pelo código da solução do problema Add Two Numbers.</em>
</p>

---

## 🧠 Conceitos Aplicados

- Estruturas de dados: listas encadeadas.  
- Manipulação de nós e ponteiros.  
- Controle de fluxo com laços e condições.  
- Tratamento de *carry* em operações matemáticas.

---

## 🧾 Arquivo principal

- [`add_two_numbers.py`](add_two_numbers.py)

---

<p align="center">
  <strong>🚀 Desenvolvido como parte dos desafios de programação LeetCode</strong>
</p>
