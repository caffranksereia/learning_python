indice_menor = 18.5
indice_normal = 18.5 and 24.9
indice_high_weight = 25.0 and 29.9
indice_Obesity_grau_1 =  30.0 and 39.9
indice_obesidade_grave = 40

menor = 'indice thinness'
normal = 'indice normal'
heigh_weight =  'indice weight'
obesity_grau_1 =  ' obesity grau 1'
obesity_grau__grave = 'obesity grau grave'

name = str(input('H r u?'))
height = float(input('What is your height?'))
weight = float(input(' what is yout weight?'))
imc = weight/(height ** 2)

if imc <= indice_menor :
    print(f'{name} have  {height:.2f} height, {weight} weight, {imc:.2f} imc, {menor} ')
elif imc <= indice_normal :
    print(f'{name} have  {height:.2f} height, {weight} weight, {imc:.2f} imc, {normal} ')
elif imc <=  indice_high_weight :
    print(f'{name} have  {height:.2f} height, {weight} weight, {imc:.2f} imc, {heigh_weight} ')
elif imc <= indice_Obesity_grau_1 :
   print(f'{name} have  {height:.2f} height, {weight} weight, {imc:.2f} imc, {obesity_grau_1} ')
else:
    print(f'{name} have  {height:.2f} height, {weight} weight, {imc:.2f} imc, {obesity_grau__grave})')
    


