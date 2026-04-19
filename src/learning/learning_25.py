"""
FLAG (Bandeira) - Marcar um local
None = Nao valor
is e is not = e ou nao (tipo, valor, identidade)
id = identidade
"""

condicao = False
passou_no_if = None
if condicao:
    passou_no_if = True
    print("faca algo")
else:
    print("nao faca algo")


if passou_no_if is None:
    print("Nao passou no if")

if passou_no_if is not None:
    print("Passou no if")
