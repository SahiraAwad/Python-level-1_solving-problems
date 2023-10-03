''' ****************************Python  Task level 3 *******************************
12. Build an email slicer : create a function that takes an email as input and retrieve the
username and domain of the email
____________________________________________________________________________________________
'''
username, domain = input('Enter your e-mail: ').split('@')
print(f'Your Username is {username} and Domain Address is {domain}')