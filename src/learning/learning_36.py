string = "ABC"
list = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
tupla = "Python", "é", "legal"


rooms = [
    ["Maria", "Helena"],
    ["Elaine"],
    [
        "Luiz",
        "Joao",
        "Eduarda",
    ],
]


# p, b, *_, ap, u = list
# print(p, b, *_, ap, u)

print(*list)
print(*string)
print(*tupla)

print(*rooms, sep="\n")
