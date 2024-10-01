class Float(object):

    def __init__(self,num,deno):
        self.nume = num
        self.deno = deno

    def __float__(self):
        return self.nume/self.deno
    
    def __str__(self) -> str:
        
        return str(self.num) +"/" + str(self.denom)
    

def main():
    a = Float(3,4)
    b = float(2,1)
    c = a*b
    print(c)

