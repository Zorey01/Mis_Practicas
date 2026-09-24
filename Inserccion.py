lista = [5, 2, 8, 1, 9, 3, 7]

for i in range(1,len(lista)):
    aux = lista[i]
    j = i-1
    while j >=0 and aux<lista[j]:
        lista[j+1]= lista[j]
        lista[j] = aux
        j-=1
print(lista)