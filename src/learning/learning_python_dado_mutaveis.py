"""
Cuidados com dados mutaveis
 =- copiando o valor (imutaveis)
 = - aponta para o mesmo valor na memoria (mutaveis)
"""

name = "Luiz"
noutra_variavel = name

name = "Joao"
print(name)
print(noutra_variavel)


list_a = ["Luiz", "Maria", 1, True, 1.2]
list_b = list_a.copy()

list_a[0] = "Qualquer coisa"

print(list_b)

# for in com listas

for name in list_a:
    print(name)
