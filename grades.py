numOfStudents = int(input('enter num of students '))
gradesList = []
valid = []
min = [0, 100]
max = [0, 0]
notValidNum = 0
sum = 0
for i in range(0, numOfStudents):
    grade = int(input())
    if(grade < 0 or grade > 100):
        valid.append(0)
        notValidNum+=1
    else:
        valid.append(1)
        sum+=grade
        if(min[1] > grade):
            min[1] = grade
            min[0] = i+1
        if(max[1] < grade):
            max[1] = grade
            max[0] = i+1
    gradesList.append(grade)

avg = sum / (numOfStudents - notValidNum)

print('num of not valid grades ' + str(notValidNum))
print(valid)

print('avg is ' + str(avg))
print('highest grade is ' + str(max[1]) + ', number ' + str(max[0]) + ' in the list')
print('lowest grade is ' + str(min[1]) + ', number ' + str(min[0]) + ' in the list')

print('grades greater than 85%:')
for i in gradesList:
    if(i >= 85 and i <= 100):
        print(str(i), str(gradesList.index(i)+1))

print('grades higher than avg:')
for i in gradesList:
    if(i > avg and i <= 100):
        print(str(i), str(gradesList.index(i)+1))
