"""
Listas em python

tipo list - mutavel

suporta varios valores de qualquer tipo
Conhecimnetos reutilizaveis - indices e fatiamento

Metodos uteis:
    append, insert, pop, del, clear, extend, +
Create read update delete

criar, lear, alterar, apagar = list [i] {crud}
"""

#        0   1   2   3
lists = [10, 20, 30, 40, 50, 60]
lists[2] = 300
# del lists[2]
# print(lists)
# print(lists[2])

lists.append(50)
lists.pop()
lists.append(60)
lists.append(70)
lists.append("80")
ult_value = lists.pop()
print(lists, "Removido", ult_value)

# insert

lists.insert(1, 5)
print(lists)

# extend

list_a = [1, 2, 3]
list_b = [4, 5, 6]

list_c = list_a + list_b
list_a.extend(
    list_b
)  # chamei o methodo exxtend e nao retorna nenhum valor de volta pois mexe diratamente na lista a

print(list_a)
