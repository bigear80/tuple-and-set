#empty tuple
data=()
print (data)
data=tuple()
print (data)
student=('vedant',13,'uithoorn','cs','cricket',[6,7,8])
print(student)
name,age,location,favorite_subject,favorite_sport,marks=student
print(name,age,location,favorite_subject,favorite_sport,marks)
# student[0]='vedant menon'
student[-1].append(675189326891)
print(student)
print(student[0:-1])
print(student[0:6:2])