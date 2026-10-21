"""
iteravel -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entrregue seu iterador
"""

texts = "Fabio"
interator = iter(texts)  # __iter__()

while True:
    try:
        print(next(interator))
    except StopIteration:
        break
