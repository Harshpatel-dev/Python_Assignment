from re import X


class Point(object):
   pointCount = 0
   def __init__(self):
      self.pointCount += 1
   
   def setX(self,x):
      self._x=x
   
   def setY(self,y):
      self._y=y

   def getX(self):
      return self._x

   def getY(self):
      return self._y
   
   def __str__(self):
      return "(" + str(self._x) + "," + str(self._y) +")"
   
   def distance(self,other):
      distx = (self._x - other._x)**2
      disty = (self._y - other._y)**2
      distancexy= (distx + disty)**0.5
      return distancexy
   @staticmethod
   def displayPointCount():
      print( "(" + str(Point.pointCount) +")")
   
   #first instance method which check whether given two points are on same axis
   def isOnSameAxis(self,other):
      if(self._x==other._x or self._y==other._y):
         print("Point p1",p1,"and p2",p2," are on same axis.")
      else:
         print("Point p1",p1,"and p2",p2," are not on same axis.")
   
   def checkQuadrant(self):
      if self._x==0 and self._y==0:
         print("Point (",self.getX(),",",self.getY(),") is origin.")
      elif self._x>0 and self._y>0:
         print("Point (",self.getX(),",",self.getY(),") is in first qudrant.")
      elif self._x>0 and self._y<0:
         print("Point (",self.getX(),",",self.getY(),") is in fourth qudrant.")
      elif self._x<0 and self._y>0:
         print("Point (",self.getX(),",",self.getY(),") is in second qudrant.")
      elif self._x<0 and self._y<0:
         print("Point (",self.getX(),",",self.getY(),") is in third qudrant.")

p1=Point()
p2=Point()

x1 = int(input("Enter point 1 x-coordinate >> "))
p1.setX(x1)
y1 = int(input("Enter point 1 y-coordinate >> "))
p1.setY(y1)
x2 = int(input("Enter point 2 x-coordinate >> "))
p2.setX(x2)
y2 = int(input("Enter point 2 y-coordinate >> "))
p2.setY(y2)

print("Distance between two points : ",p1.distance(p2))
p1.isOnSameAxis(p2)
# p1.displayPointCount()
p1.checkQuadrant()