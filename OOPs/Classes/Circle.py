# defining circle class
class Circle(object):
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius

    def is_inside(self, point):
        """return if the point is in the self otherwie return false"""
        return point.distance(self.distance) <self.radius
    
        


    
# circle object is created
center = Coordinate(2,2)

c1 = Circle(center,2)
p = Coordinate(1,1)
print(c1.is_inside(p))

