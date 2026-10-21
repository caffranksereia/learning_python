import os

secrety_keyword = "Abobora"
lettra_right = ""

i = 3
while i > 0:
    lettra = input("digite:")
    i -= 1

    if len(lettra) > 1:
        print("digite apenas uma letra.")
        continue

    if lettra in secrety_keyword:
        lettra_right += lettra

    format_word = ""
    for lettra_secrety in secrety_keyword:
        if lettra_secrety in lettra_right:
            format_word += lettra_secrety
        else:
            format_word += "*"
    print(format_word)

    if format_word == secrety_keyword:
        os.system("cls")
        print("Ganhou! Parabens")
        print(secrety_keyword)
        print("Tentativas:", i)
        lettra_right = ""

        i = 0
