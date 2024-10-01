class SimpleFraction(object):
    
    def __init__(self,num,deno):
        self.num = num
        self.deno = deno

    def get_reverse(self):
        """Return a float representing 1/self    """
        # write your code here
        return self.denom/self.num 
        

 
   
    def invert(self):
        """set the self's numerator to its denominatior and vice versa"""
            #   write your code here
            # 
            #  
        # (self.num , self.deno) = (self.deno,self.num)
        """Other ways to the same thing is"""
        newnum = self.deno
        newdeno = self.num 
        self.num = newnum
        self.deno = newdeno



  
        

f1 = SimpleFraction(3,4)
print(f1.num , f1.deno)
# print(f1.get_reverse)
f1.invert()
print(f1.num , f1.deno) 
