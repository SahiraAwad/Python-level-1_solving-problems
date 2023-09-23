'''            *************problem 2:********************
    
            2-Create a python function that takes 2 numbers
              x,y and prints all the numbers between 1 and 100
              that can be divided on x,y
'''
#Here is the solution

def print_numbers_divided_on(x,y):

    for i in range(1,101):
         if i%x==0 and i%y==0:
             print (i)
        




print('Enter the first number x:')
x=int(input())

print('Enter the second number y:')
y=int(input())
print ('All the divided numbers on x,y')
print_numbers_divided_on(x,y)
