marks = int(input('Enter The Marks: '))

if (marks > 100):
    print("Please Enter correct marks")
    exit()

if (marks >= 90):
    grade = 'A'

elif (marks >= 80):
    grade = 'B'

elif (marks >= 70):
    grade = 'C'

elif (marks >= 60):
    grade = 'D'

else: 
    grade = 'F'

print("Grade ",grade)