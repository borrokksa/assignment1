#!/usr/bin/env python
# coding: utf-8

# In[ ]:
#question 9

import random

number = random.randint(1, 10)
guess = 0 

while guess != number and guess != "exit":
    guess = input("Please guess a number between 1 and 9. When you want to end the game print 'exit': ")

    if guess == "exit":
        print("Game Over")
        break
        
    guess = int(guess)

    if guess not in range(1, 10):
        print("You have to guess a number between 1 and 9!")
    elif guess < number:
        print("You've guessed too low!")
        print("The hidden number is " + str(number) )
    elif guess > number:
        print("You've guessed too high!")
        print("The hidden number is " + str(number) )
    else:
        print("You rock! You've got it at the first try!")
         
        print("The hidden number is " + str(number) )


# In[12]:
#question 20

a = [1, 3, 5, 30, 42, 43, 500]

q=int(input('Which number do you want to look for?'))
flag = 0 
while a != []:

    #print(a)

    mid=int(len(a)/2)

    #print(a[mid])

    if q==a[mid]:

        print('The list contains %d.' % q)
        flag = 1
        break

        

    elif q>a[mid]:

        #print('higher')

        del a[:mid+1]

 

    elif q<a[mid]:

        #print('lower')

        del a[mid:]

 

   
#print(a)

 
if not flag == 1 :
    print('''The list doesn't contain %d.''' % q)


# In[ ]:




