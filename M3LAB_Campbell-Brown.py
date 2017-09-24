# CTI-110 
# M3Lab-Grades
# Name Alicia Campbell-Brown
# Date 9-24-2017


def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores
A_score = 90    
B_score = 80
C_score = 70
D_score = 60
F_score = 50
    
grade = eval(input('Enter grade: '))

if grade >= A_score:
    print('Your grade is: A')

elif grade >= B_score:
    print('Your grade is: B')
elif grade >= C_score:
    print('Your grade is: C')
elif grade >= D_score:
    print('Your grade is: D')

elif grade >= F_score:
    print('Your grade is: F')









# program start
main()
