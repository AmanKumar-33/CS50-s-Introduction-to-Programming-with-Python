# in python enumeartes present the values of index of each _ - _thing

# enumarete(iterable, start = 0)
students = ["aman","Lovely","Raja"]

for _ in range(len(students)):
    print(_+1, students[_])

# other way to do the same thing by enumrates
""""
for i, student in enumerate(students):
    print(i+1,student)

"""