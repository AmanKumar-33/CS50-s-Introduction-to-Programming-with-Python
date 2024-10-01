students = [
    {"name":"Harry","house":"gryffindor"},
    {"name":"Harmione","house":"gryffindor"},
    {"name":"Ron","house":"gryffindor"},
    {"name":"Draco","house":"slytherine"},

]

gryffindors = [
    student["name"] for student in students if student["house"] == "gryffindor"

]
for gryffindor in sorted(gryffindors):
    print(gryffindor)