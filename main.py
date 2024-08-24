lista = [1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4]
lista_sem_repeticao = []

for item in lista:
  if item not in lista_sem_repeticao:
    lista_sem_repeticao.append(item)

print(lista_sem_repeticao) # Saída: [1, 3, 2, 4, 5, 7, 6, 8]