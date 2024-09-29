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
    


f1= fraction(3,4)
f2 = fraction(4,5)
f3 = fraction(5,1)  
print(f1)
print(f2)
print(f3)
