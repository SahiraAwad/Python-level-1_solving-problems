'''problem6:
Create a function that takes a sentence
and word and remove the word from the sentence
'''
#Here's the solution

def removeword_fromsentence(s,w):
    listofword= s.split(' ')
    for i in   listofword:
        if i == w:
            listofword.remove(i)
            
    print('Sentence after remove the word:',' '.join( listofword))

    
print('Enter the sentence :')    
s= input('')
print('Enter the word that should be deleted')
w= input('')
removeword_fromsentence(s,w)
