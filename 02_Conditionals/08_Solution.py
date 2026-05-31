password = 'Malik12@'
# password_len = len(password)

if (len(password) < 6):
    strength = 'weak'

elif (len(password) <= 18):
    strength = 'Medium'

else:
    strength = 'Strong'

print('Password Strength is: ', strength)