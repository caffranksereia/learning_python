"""\
    basic string interpolation

    s - string
    d e i - int
    f - float
    x e X - Hexadecimal (abcdef0123456780)

"""


name ='Fabio'
price = 1000.000
variable = '%s, Fabio, o preco R$%.2f'% (name, price)
variable_hexa = 'o hexadecimal de %d e %08X' % (1500, 1500)
print(variable)
print(variable_hexa)