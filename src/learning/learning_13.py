'''

    format 

'''

a = 'A'
b = 'B'
c = 1.1
string = 'a={1}, b={0}, c={name:.2f}'
formating =string.format(a,
                         b,
                         name = c
                         )

print(formating)