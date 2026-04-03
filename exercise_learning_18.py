first_number = int(
    input('Choose one number:')
    )
second_number = int( 
    input('choose second number')
    )

if first_number > second_number and first_number >= second_number:
    print(f'first number {first_number=} is greater than or equal to second {second_number=}')
elif first_number < second_number and first_number <= second_number:
    print(f'first number {first_number=} is less than or equal to second {second_number=}')
elif first_number == second_number:
    print(f'first number {first_number=} is equal to second {second_number=}')
elif first_number != second_number:
    print(f'first number {first_number=} is not equal to  {second_number=}')
else:
    print('nothing here')