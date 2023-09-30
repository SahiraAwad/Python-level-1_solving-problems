'''problem8:
Create a function that takes x,y and prints all the
number that can be divide by y from x to 100
'''

#Here is the solution

def print_numberdeivedby_y(x,y):
    for x in range(x,101):
        if x%y==0:
           
            print(x)
try:
    
    print('Please enter  x,y ')
    x = int(input());y = int(input())
    
except ValueError:
    print('please enter integer')



print('All the numbers that are divided by y')
print_numberdeivedby_y(x,y)
