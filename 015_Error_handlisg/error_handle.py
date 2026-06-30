file = open('youtube.txt', 'w') #write mode if file not created then it will create file

try:
    file.write('Learning Python')
finally:
    file.close()

#Second Method
with open('youtube.txt', 'w') as file:
    file.write('Python Code')