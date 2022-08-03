class Point:
    pointCount =0

    def __init__(self,xVal,yVal):
        self.x=xVal
        self.y=yVal
        Point.pointCount += 1

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) +")"

    def distance(self,other):
        distx = (self.x - other.x)**2
        disty = (self.y - other.y)**2
        distancexy= (distx + disty)**0.5
        return distancexy

    @staticmethod
    def displayPointCount():
        print( "(" + str(Point.pointCount) +")")
    
