students = [
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Harmione","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"slytherine"},

]
# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"
# in case of lamda the code can be more simple as we use //lamda s:s["house"] == "gryffindor"
# gryffindors = filter(is_gryffindor,students)
"""we have used lamda here which reduce our code //is_gryffindor"""
gryffindors = filter(lambda s: s["house"] == "Gryffindor",students)


for gryffindor in sorted(gryffindors, key = lambda s: s["name"]):
      print(gryffindor["name"])