''' problem4:
create a function that takes a sentence
and prints the sentence without duplicated words    

'''

# Here's the solution

def remove_duplicated_word(s):
   

    list=s.split(' ')
    new_list=[]
    for w in list:
        if w not in new_list:
            new_list.append(w)
            
    print(' '.join(new_list))   
  
print('Enter the sentence:')       
s= input('')
print('The sentence without duplicated word')
remove_duplicated_word(s)
