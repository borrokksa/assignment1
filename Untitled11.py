#!/usr/bin/env python
# coding: utf-8

# In[1]:
#question 1

name = input("Enter your name ")
age = int(input("Enter your age "))
year = str(((2020 - age)+100))
print(name + " will be 100 years old in the year " + year)


# In[2]:

#question 2
num = int(input("Enter a number "))

if num % 2==0 :
    print("It is a even number ")
else:
     
    print("It is a odd number ")


# In[3]:
#question 3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:

    if i < 5:

        print(i)


# In[4]:
#question 4

x = int(input("enter a number "))

listRange = list(range(2,x))

divisorList = []

for number in listRange:
    if x % number == 0:
        divisorList.append(number)

print(divisorList)


# In[5]:
#question 5

a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a) & set(b) 
print(c)


# In[6]:
#question 6

a=input("enter a word")
b=a[::-1]
print(b) 
if a == b:
    print("palindrome")
else:
    print("not a palindrome")


# In[10]:
#question 7

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
b = [i for i in a if i % 2 == 0]

print(b)


# In[1]:
#question 8

a1 = input("Player 1 choose rock, paper or scissors? ")
a2 = input("Player 2 choose rock, paper or scissors? ")

if a1 == a2:
        print("It's a tie!")
elif a1 == 'rock':
        if a2 == 'scissors':
            print("Rock wins!")
        else:
            print("Paper wins!")
elif a1 == 'scissors':
        if a2 == 'paper':
            print("Scissors win!")
        else:
            print("Rock wins!")
elif a1 == 'paper':
        if a2 == 'rock':
            print("Paper wins!")
        else:
            print("Scissors win!")
else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




