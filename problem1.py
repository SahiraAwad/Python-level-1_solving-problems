'''               ***************problem 1:****************
           1- Create a python function that takes 2 numbers x,y
           and prints 2 lists containing the odd and even numbers in
           the x,yrange

           -------------------------------------------------------------

'''

#Here's the solution

def Return_lists_even_odd (x,y):
    even_list =[]
    odd_list = []
    k=0
    f=0

    for x in range(x,y+1):
        if x%2==0:
            
            even_list.insert(k,x)
            k+=1
      
        else:
            odd_list.insert(f,x)
            f+=1
            
    print('List of even numbers between x and y :',even_list)
    print('List of odd numbers between x and y :',odd_list)
    
print('Enter the first number x:')
x=int(input())

print('Enter the second number y:')
y=int(input())

# Call the function 
Return_lists_even_odd(x,y)













