"""
Imprecisao de ponto flutuante
double-precision floating-point format IEEE 754
"""

import decimal

number_1 = decimal.Decimal('0.1')
number_2 = decimal.Decimal('0.7')

number_3 = number_1 + number_2
print(number_3)

print(f"{number_3:.2f}")
print(round(number_3,2))