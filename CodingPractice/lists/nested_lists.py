'''
@author: Solrac
'''

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    
grades = []
students_2low = []
for i in range(len(students)):
    grades.append(students[i][1])
    grades.sort()
    #if i == 1:
    #    continue 
    #if grades[i] == grades[1]:
    #    students_2low.append(students[i])

for i in range(len(grades)):
    if students[i][1] == grades[1]:
        students_2low.append(students[i][0])

students_2low.sort()

for i in students_2low:
    print(i)