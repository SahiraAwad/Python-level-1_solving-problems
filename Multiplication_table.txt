'''      ******************problem 3:********************
Create a python function that takes 2 numbers x, y
and prints the multiplication table from x to y

__________________________________________________________
'''

#Here 's the solution


def Multiplication_table(x,y):
   
    k=1

    for x in range(x,y+1):
        print(f'Muliplication table of {x}')
        for k in range (1,13):
            print (f'{x} X {k}\t ={x*k}')
        print('************')    

print('Enter the first table :')
x=int(input())

print('Enter the last table:')
y=int(input())
print('Here is the Multiplication tables:')
Multiplication_table(x,y)
