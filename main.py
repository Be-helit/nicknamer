import random
#The library for doing random stuff
name=''
#Initialising The name var
syl=int(input('Syllable?'))
#asking from the user the stllable they want
z=int(1)
#initialising Counter 
while z<=syl:
    name=name+random.choice('bcdfghjklmnpqrstvwxyz')
    name=name+random.choice('aeiou')
    z=z+1
    
#Firing the loop
print(name)
#printing the name
