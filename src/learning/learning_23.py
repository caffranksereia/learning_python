"""
    
    introduce to try/except
    try -> used to runnin a block of code
    except -> used to catch and handle errors 
    that occur during execution

"""
user_input_str = input('dobro:')

try:
    print('STR', user_input_str)
    number_f = float(user_input_str)
    print('FLOAT:', number_f)
    print(f'O dobro de {user_input_str}: {number_f * 2:.2f}')
except:
    print('Isso nao e numero')


#verificar se tem numero digito e retorn um bool isdigit()

#if user_input_str.isdigit():
#    
#else:
#    )
    
