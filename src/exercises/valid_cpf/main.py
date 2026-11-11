"""_summary_
CPF: 746.824.890 - 70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem  regressiva comecando de 10

ex: 746.824.890-70 (74682489070)
    10 9 8 7 6 5 4 3 2
*  7   4  6 8 2 4 8 9 0
    70 36 48 12 29 32 27 0

    Somar todos os resultados:
    70+36 +48 +12 +29 +32 +27 +0 = 301
    Multiplicar o resultado anterior por 10
    301 * 10 = 3010
    Obter o resto da divisao da conta anterior por 11
    3010 % 11 = 7

    se o  resultado anterior for maior que 9:
        resultado e 0
    contario disso:
        resultado e o valor da conta

primeiro digito do cpf é 7

"""

regress_count = 10

register = input("What's your cpf:")
new_register = register.replace(".", "").replace("-", "").strip()

result = 0
if len(new_register) == 11 and new_register.isdigit():

    numbers = [int(digit) for digit in new_register[:9]]

    for _ in range(2):
        regress_count = len(numbers) + 1
        result = 0

        for index, digit in enumerate(numbers):
            result += digit * (len(numbers) + 1 - index)

        new_digit = (result * 10) % 11
        new_digit = new_digit if new_digit <= 9 else 0

        numbers.append(new_digit)
    cpf_calculated = "".join(map(str, numbers))

    if new_register == cpf_calculated and len(set(new_register)) > 1:
        print("register valid")
    else:
        print("register invalid")

    print(f"register calculed:{ cpf_calculated}")
else:
    print("Register can 11 numbers")
