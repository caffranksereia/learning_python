""""
lista e seus indeces

"""

rooms = [
    ["Maria", 'Helena'],

    ['Elaine'],

    ['Luiz', 'Joao', 'Eduarda',(0,10,20,30,40)],
]

# print(rooms[1][0])
# print(rooms[0][1])
# print(rooms[2][2])
# print(rooms[2][3][3])

for room in rooms:
    print(f'the room e {room}')
    for aluno in room:
        print(aluno)
