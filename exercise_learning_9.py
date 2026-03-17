print('-------------------------------------')
print('         arithmetic operator         ')
print('-------------------------------------')

number = 10
second_number = 5
#you can do anything with int and float

addition = number + second_number

subtraction = number - second_number

multiplication = number * second_number

"""
    Division always returns a float, even when the numbers are integers.
"""
division = number / second_number
#its doesnt always return an integer and truncates
integer_division = number // second_number 

exponentiation = number ** second_number
#rest division 
modulus = number % second_number


print('-------------------------------------')
print('               result                ')
print('-------------------------------------')
print('addition',addition)
print('subtraction',subtraction)
print('multiplication',multiplication)
print('division',division)
print('integer division',integer_division)
print('exponentiation',exponentiation)
print('modulus',modulus)
print('-------------------------------------')
