#!/usr/bin/env python
# coding: utf-8

# In[9]:
#question 10

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(*[item for item in a if item  in b])


# In[30]:
#question 11

n = int(input(print("Enter a number: ")))
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(n))


# In[31]:
#question 12

a = [5, 10, 15, 20, 25]
def list_ends(a):
    return [a[0], a[len(a)-1]]
print(list_ends(a))


# In[35]:
#question 13

def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib
print(gen_fib())


# In[40]:
#question 14

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      

print(Remove(duplicate)) 


# In[41]:
#question 15

def phraseReverse(string):
    list1 = string.split(' ')
    list1.reverse()
    list1 = ' '.join(list1)
    return list1

question = input('Please enter a phrase: ')
answer = phraseReverse(question)
print(answer)


# In[44]:
#question 16

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print(p)


# In[ ]:
#question 18

import random
import array as arr
r=random.randint(1000,9999)
print(r)
n=input("Input any four digit number")
n=int(n)
p=arr.array('b',[0,0,0,0])
q=arr.array('b',[0,0,0,0])
while r!=n:
    b=0
    c=0
    r1=r
    for x in range(4):
        p[x]=r1%10
        q[x]=n%10
        r1//=10
        n//=10
    for x in range(4):
        if(p[x] is q[x]):
            c+=1
        elif p[x] in q:
            b+=1

    print(b,"bulls ",c,"cows")
    n=input("Input any four digit number")
    n=int(n)
if r==n:
    print("your number matches")
        


# In[ ]:





# In[ ]:




