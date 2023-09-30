'''problem5:
. Create a function that takes a sentence
and prints how many words in the sentence
(do not count the spaces)
'''

# Here is the solution

def sentence_numberofword (s):
    listofwords=s.split(' ')
    if len(listofwords)> 1:
        print('Number of words are:',len(listofwords))
    else:
        print('Number of words is:',len(listofwords))
        
print('Enter the sentence:')
s= input('')
sentence_numberofword (s)  
