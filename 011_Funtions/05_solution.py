user = input('Enter the name: ')

def greets(name='Malik'):
    print('Hey! this is', name)

if user:
    greets(user)
else:
    greets()