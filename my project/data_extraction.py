from numpy import *
from pandas import *
from user_data_training import *

f = open("Course-List.txt", 'r')
courses = [i.rstrip() for i in f.readlines()]
f.close()

course_with_index = {}
for i in range(len(courses)):
    course_with_index[courses[i]] = i

training_data = zeros((4500, 150), dtype=int)
user = 0
for i in training:
    for j in training[i]:
        training_data[user][course_with_index[j]] = training[i][j]
    user += 1

DataFrame(training_data).to_csv("temp.csv")

'''f = open("training_data.txt",'w')
f.write("[")
for i in range(4500):
    f.write("[")
    for j in range(150):
        if j < 149:
            f.write("%d,"%training_data[i][j])
        else:
            f.write("%d"%training_data[i][j])
    f.write("],")
f.write("]")
f.close()'''