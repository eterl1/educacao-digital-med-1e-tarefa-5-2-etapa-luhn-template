cartao = input().strip()

# transforma cada dígito em inteiro dentro de uma lista
digitos = [int(d) for d in cartao]

# soma dos dígitos nas posições ímpares (da direita, de 2 em 2)
impares = sum(digitos[-1::-2])

# para os pares (da direita, também de 2 em 2)
pares = []
for d in digitos[-2::-2]:
    dobro = d * 2
    if dobro < 10:
        pares.append(dobro)
    else:
        pares.append(dobro - 9)  # equivalente a "dobro - 10 + 1"
        
# soma total
total = impares + sum(pares)

# validação
if total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")

