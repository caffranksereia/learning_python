VARIAVEL = "i e 2, pulando ..."
VARIAVEL_2 = "i e 8, seu else nao executara"
VARIAVEL_3 = " for completo com sucesso"

for i in range(10):
    if i == 2:
        print(VARIAVEL)
        continue

    if i == 8:
        print(VARIAVEL_2)
        break

    for j in range(1, 3):
        print(i, j)

else:
    print(VARIAVEL_3)
