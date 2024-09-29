students = ["Harry","Herminoe","Ron"]

""" gryffindors = []"""

# for student in students:
#     gryffindors.append({"name":student,"house":"Gryffindor"})
# to reduce the number of complexity of cody here we have used dict in list where we finding student with there houses
gryffindors = [{"name":student, "house":"gryffindors"} for student in students ]

print(gryffindors)

# dict comprehension
# in dict comprehension we dont need to write every thing 
print("At here we have done dict comprehension")

gryffindors1 = {student : "Gryffindors" for student in students}
print(gryffindors1)