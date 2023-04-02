#This game is too hard to whrite so if you did it, YOU SO GREAT.

import random as r
x = int(input('Tell me the answer in silence:'))
b = int(input('karan bozorg? '))
k = int(input('karane kuchak? '))
print('jadval halat ha:')
print('[ Right , Larger , Smaller ]')
n = r.randint(k,b)
print(n)
A = input('How is the number? ')
while A != 'Right':
     if A == 'Smaller':
        n = r.randint(k,n)
        print(n)
        A = input('What about now? ')
     elif A == 'Larger':
        z = r.randint(n,b)
        print(n)
        A = input('What about now? ')

        
if A == 'Right':
    print('That is my number!!!')