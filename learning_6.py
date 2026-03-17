"""
- Conversao de tipos, coercao
- type conversion( typecasting, coercion)
its process of converting one date tupe into another

primitive and immutable types:
str, int, float and bool


"""

print(1 + 1) #added
print( 'a' + 'b') #concat
#this happens in dynamic languages. when you pass two types to  the interpreter, its knows what to do.

print( 'a' + 'b') #concated
#print('1' + 1) An error can occur when the interpreter tries to concatenate a str with an int 

#str, int, float, bool are imuutable
#there are ways to convert one type into another
print('1', type('1')) #o numero virou string pois esta em entre os single marks
#A number becomes a string its enclosed in single marks

print(int('1'), type(int('1'))) #convert str to int
#you can add it by converting

print(int('1' ) + 1)
#you can convert it to a float
print(float('1') + 1)

#you can convert it a bool if it has only possible values:  True and false 
print(bool('')) #string null considered false

#coecion

print(str(11) + 'b')

