class fraction(object):
    def __init__(self,n,d):
        self.num = n
        self.denom = d

    def __str__(self):
        """Concatenation means every piece has to be a str"""
        # modifying the problem
        if self.denom == 1:
            return str(self.num) 
        return str(self.num) +"/" + str(self.denom)
    


# """Dunder method for multiplication"""

    def multi(self,oth):
       top = self.num * oth.num
       bottom = self.deno * oth.deno
       return top/bottom 

    # """dender method of __mul__"""
    # def __mul__(self,other):
    #     top = self.num * other.num
    #    bottom = self.deno * other.deno
    #    return fraction(top/bottom)



f1= fraction(3,4)
f2 = fraction(4,5)
f3 = fraction(5,1)  
print(f1)
print(f2)
print(f3)
c = f1*f2
print(c)

