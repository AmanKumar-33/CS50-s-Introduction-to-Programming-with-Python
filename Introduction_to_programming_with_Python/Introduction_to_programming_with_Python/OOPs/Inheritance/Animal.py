class Animal(object):

    """Special method to create an instance """
    def __init__(self, age):    
        """self Variable to refer to the instance of the class"""
        self.age = age 
        self.name = None

    def __str__(self):
        return "Animal" +":"+ str(self.name) + ":" + str(self.age)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age = newage
    def set_name(self,newname =""):
        self.name = newname

# creating the instance of the class
# a = Animal(4)
# # print(a)
# b = Animal(9)
# print(b)
# a.set_name("amam")
# print(a)
def animal_dict(L):
      """L is a list 
      Return a dictionary d,mapping an int to animal object """

      """dictionary is created"""
      d = { }
      for n in L:
          if type(n) == int and n >= 0:
              d[n] = Animal(n)
      return d


# L = [2,5,'q',0,'a']

"""manually loop over animal object and acess their data attribute through getter method"""

# Animals = animal_dict(L)
# for n,a in Animals.items():
#     print(f'key{n} with value {a}')

# print(Animal)

def make_animal(L1,L2):
    """L1 is the list of int 
        L2 is the list of string
        L1 and L2 have the same length
        create an list of animals the same lengthas L1
        and an animal object at same index i has the age and name
        """
    # L3 = []
    # for i in range(len(L1)):
    #     # i = 0,1,2,3,4,5
    #     age = L1[i]
    #     name = L2[i]
    #     a = Animal(age)
    #     a.set_name(name)
    #     L3.append(a)
    # return L3









# L1 = [2,5,7]
# L2 = ['doggy','rocky','salmon']
# dogs = make_animal(L1,L2)
# for i in dogs:
#     print(i)

"""Here we are going to make cat as hierarche of Animal class"""
class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "Cat :" +str(self.name) +":" +str(self.age) 
    
# c = Cat(5)
# c.set_name("fluffy")
# c.speak()

# print(c)

class Rabbit(Animal):

    def speak(self):
        print("chikk")

    def __str__(self):
        return "Rabbit : " +str(self.name) + ":" + str(self.age)

class Human(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        self.set_name(name)
        self.friends = []
    def get_friend(self):
        return self.friends.copy()
    def add_friends(self,friname):
        if friname not in self.friends:
            self.friends.append(friname)
    def speak(self):
        print("Hello")
    def age_difference(self,other):
        age_diff= self.age - other.age
        print(abs(age_diff),"year difference ")
    def __str__(self):
        return "Human :" +str(self.name) + ":" + str(self.age)

# p1 = Human('Aman',27)

# print(p1)
# p1.speak()


def make_pets(d):
    """d is a dict mapping a human obj to cat obj 
    prints, on each line, the name of the person, a colon and the name of the person cat
    """
    # d = {}
    for k,v in d.items():
        # k is person and v is cat  Like aman: fluffy
        print(k.get_name() + ':' + v.get_name())




    
p1 = Human("aman",27)
p2 = Human("james",22)
c1 = Cat(1)
c1.set_name("fluffy")

c2 = Cat(3)
c2.set_name("chikka")

d = {p1:c1,p2:c2}
make_pets(d)














    

    





