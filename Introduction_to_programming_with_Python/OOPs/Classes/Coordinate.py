#writing an code for finding the coordinate in 2d axis

# defination of the object 
class Coordinate(object):
    """A cordinate made up of an x and y values """
    def __init__(self,xval,yval):
        """set the x and y value """
        self.x = xval
        self.y = yval
    # method 
    # 1) Procedural attribute 
    # 2)Python always pass the object as first argument
    #        use self
    def Distance(self,other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        """return the euclidian object """
        return (x_diff_sq + y_diff_sq)**0.5
        # return  

# making new the object 
c = Coordinate(4,3)
origin= Coordinate(0,0)
print(c.x)
print(origin.y)
print(c.Distance(origin))
