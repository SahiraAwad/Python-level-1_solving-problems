'''prblem 7:
    
Create a function takes a sentence and a word and
prints how many time the word used in the sentence
'''
#Here is the solution


def frequentofword_insentence(s,w):
    frequentofword=s.count(w)
    print(f'frequnecy of word is {frequentofword} times')
    

print('Enter the sentence')
s= input('')
print('Enter the word to check out')
w= input('')
frequentofword_insentence(s,w)
