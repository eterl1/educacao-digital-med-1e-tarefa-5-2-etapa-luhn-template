# ✅ Conferência de Cartão — Algoritmo de Luhn

**Atividade individual** (treino para a prova).  
Implemente em `student.py` um programa que leia **uma linha** com o número do cartão (apenas dígitos) e **imprima**:

- `Cartão válido`  (se passar no Luhn)
- `Cartão inválido` (caso contrário)

---

## Luhn
O algoritmo de **Luhn** verifica se um número de cartão é **possível**. Em resumo:
1) Partindo da direita (sentido negativo).  
2) Some os dígitos em posição ímpar.  
3) Some o dobro dos dígitos em posição par (se esse dobre estiver entre 10 e 18 - inclusive- some os dígitos do resultado, por exemplo 12 -> 3).
4) Some os resultados.  
5) Se a soma for múltipla de 10, o cartão é válido.

---

## Dicas para implementar

1. **Insira cada dígito** do `input` em uma **lista vazia**, já **transformando em inteiro**.
2. Para pegar os **dígitos ímpares**, selecione do **final** pulando de 2 em 2 e **some** essa lista.
3. Para os **dígitos pares**, selecione a partir de -2 e insira em uma lista o dobro do dígito, se o dobro <10; ou o dobro do dígito menos dez mais um.
4. **Some a lista dos pares recalculados** (pelo algoritmo).
5. **Some** (ímpares) + (pares dobrada).
6. **Teste se é múltiplo de 10**: `int(n/10) == n/10` (ou `n % 10 == 0`).
7. **Imprima** exatamente `Cartão válido` **ou** `Cartão inválido`.


---

## Entrada / Saída
- **Entrada**: uma linha com dígitos do cartão (ex.: `4111111111111111`).  
- **Saída**: `Cartão válido` **ou** `Cartão inválido`.

---

