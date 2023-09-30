'''                    Python Task Level 2 :
Names = [‘mahmoud’,’farida’,’ali’,’hassan’,’mohamed’,’khaled’,’taha’]
Using the names list above create a python code that :
1. Transform all names to uppercase using
[normal list - list comprehension - functional programming
'''
# convert list into uppercase
#1- solution using Normal list(with 2 ways)
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

new_string = (' '.join(Names))
upper_string = new_string.upper()
list= upper_string.split(' ')
print(list)

# Using for loop
New_list=[]
for i in  names:
  New_list.append(i.upper())
    
print(New_list)


#2- solution using comprehension list(1)
names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

New_list=[ i.upper()  for i in names]
print(New_list)


#3- solution using comprehension list(2)
names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
def upper_case(i):
  return i.upper()
x=list(map(upper_case, names))

print(x) 
#Or using lambda
x=list(map(lambda i:i.upper(), names))

print(x)


'''
2. Get the names that contains ‘a’ in a list
using [normal list - list comprehension - functionalprogramming]

'''

names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

#1
for i in names:
  if 'a' in i:
    print(i)
    

#2 list comprehension 
list_word=[i for i in names if 'a' in i]    
print(list_word)

#3 functional programming
def condition(i):
  if 'a' in i:
    return i
list_word = list(map(condition,names))
print(list_word)

#Another way
list_word = list(map(lambda i: i if 'a' in i else None ,names))
print(list_word)
'''
3. Get the names that starts with ‘t’ in a list using [normal list - list comprehension - functional
programming]

'''
#1

for i in names:
  if i[0]=='t':
    print(i)
    

#2
    
list=[i for i in names if i[0]=='t']
print(list)


#3
names = ['mahmoud','talal','farida','ali','hassan','mohamed','khaled','taha']


s= list(filter(lambda i: i if  i[0]=='t' else None,names))


print(s)

#*************************************************************
#. Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional
#programming]
#1-

names = ['mahmoud','talal','farida','ali','hassan','mohamed','khaled','taha']
k=0

for i in names:
  s=i.count('a')
  if s>=2:
    
#2
names = ['mahmoud','talal','farida','ali','hassan','mohamed','khaled','taha']
list_word_containa =[i for i in names if (i.count('a')>=2)  ]
print(list_word_containa )

#3

names = ['mahmoud','talal','farida','ali','hassan','mohamed','khaled','taha']

new= list(filter(lambda i: i if (i.count('a')>=2) else None, names))
print(new)

#**********************************************************************
#5. Print a list contains the len of each word in the list using [normal list - list comprehension -
#functional programming
names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
#normal list
list_of_length=[]
for i in names:
  list_of_length.append(len(i))


print(list_of_length)

#list comprehersion
list_of_length=[len(i) for i in names ]
print('The length of words in the list as follow')
print(list_of_length)

# functional programming

list_of_length=list(map(lambda i: len(i),names))
print('The length of words in the list as follow')
print(list_of_length)
  
  
#*********************************************
'''
6. Unpack the list in
7. a,b , a= the first index , b = rest of the list
8. a = the first index , b = the last index
9. a = the first index , b = the second index

'''

#solution

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

#7
a,*b= Names
print(a,b)
#8
a,*_,b= Names
print(a,b)
#9
a,b,*_= Names
print(a,b)

