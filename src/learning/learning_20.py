"""
    formatacao basica de strings
    s - string
    d - int
    f - float
    <numero de digitos>f
    x ou X - hexadecimal
    (Caracteres)(><^)(quantidade)
    > - Esquerda
    < - Direita
    ^ - Centro 
    = - forca o numero aparecer antes dos zeros
    Sinal - ou +
    ex.: 0>-100, .1f
    conversion flags - !r !s !a

"""

variable = 'ABC'
variable_num = 1000.09708176
variable_hexa = 'o hexadecimal de'
print(f'{variable}')
print(f'{variable: >10}')
print(f'{variable: <10}.')
print(f'{variable:$^10}')
print(f'{variable:$<10}.')
print(f'{variable:$<10}.')

'Number variable'
print(f'{variable_num:0=+10,.1f}')\

' Hexadeciaml variable'
print(variable_hexa,f'{1500:08x}')

'converion flags'
print(f'{variable!r}')