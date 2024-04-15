'''Dictionary Comprehension'''
import random

names = [ "prakash","Anushka","amit","om"]
# {new_key:new_value for items in list}
students = {student:random.randint(1,100) for student in names}
print(students)

passed_students = {student:score for (student,score) in students.items() if  score>=50 }
print(passed_students)

students_dict = {
    "student" : ["Namit", "Nilesh", "Praful"],
    "score" : [82,78,99]
}

import pandas
student_dataframe = pandas.DataFrame(students_dict)

for (index,row) in student_dataframe.iterrows():
    print(row.student)
    print(row.score)