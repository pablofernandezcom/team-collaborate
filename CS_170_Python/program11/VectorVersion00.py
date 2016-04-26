# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:48:58 2016

@author: Tyler
"""

class Vector:
    """ A class to represent 2D Vectors, i.e. <1,2>. """
    def __init__(self,x=0,y=0):
        """ Create a new Vector object. """
        self.x = x
        self.y = y
        """        
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        """

    def __str__(self):
        """ Convert to string for printing purposes. """
        return "<{0},{1}>".format(self.x,self.y)

    def __eq__(self,other):
        """ Test equality of Vector objects using ==. """
        if 

    def __ne__(self,other):
        """ Test inequality of Vector objects using !=. """
        pass

    def __add__(self,other):
        """ Add two Vector objects using the + operator. """
        pass

    def __mul__(self,a):
        """ Perform scalar multiplication using the * operator. """
        pass

    def __rmul__(self,a):
        """ Perform scalar multiplication using the * operator. 
        Allows the scalar to appear on the left of the Vector."""
        pass
        
    def __iadd__(self,other):
        """ Perform Vector increments using the += operator. """
        pass
    
    def setX(self, x):
        """ Set the x coordinate. """
        pass
    
    def setY(self, y):
        """ Set the y coordinate. """
        pass

    def getX(self):
        """ Return the x coordinate. """
        pass
    
    def getY(self):
        """ Return the y coordinate. """
        pass

if __name__=="__main__":
    import sys
    def test(did_pass):
        """  Print the result of a test.  """
        linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)
        
    # Test the __str__ function
    v = Vector(1,-2)
    test(str(v)=="<1,-2>")

    # Test the __eq__ function
    v = Vector(1,-2)
    w = Vector(1,-2)
    test(v == w)

    v = Vector(1,-2)
    w = Vector(0,-2)
    test(not (v == w))

    v = Vector(0,-2)
    w = Vector(1,-2)
    test(not (v == w))

    v = Vector(0,0)
    w = Vector(1,-2)
    test(not (v == w))
    
    # Test the __ne__ function
    v = Vector(1,-2)
    w = Vector(1,-2)
    test(not(v != w))

    v = Vector(1,-2)
    w = Vector(0,-2)
    test(v != w)

    v = Vector(0,-2)
    w = Vector(1,-2)
    test(v != w)

    v = Vector(0,0)
    w = Vector(1,-2)
    test(v != w)
    


    # Test the __add__ function
    v = Vector(1,-2)
    w = Vector(3,4)
    test(v+w == Vector(4,2))
    test(w+v == Vector(4,2))

    # Test the __mul__ function
    v = Vector(1,-2)
    test(v*2 == Vector(2,-4))
    test(2*v == Vector(2,-4))
    
    # Test the __iadd__ function
    v = Vector(1,-2)
    v += Vector(1,1)
    test(v==Vector(2,-1))
    
    # Test the setX, setY functions.
    v = Vector(2,4)
    v.setX(-1)
    v.setY(2)
    test(v==Vector(-1,2))
    
    # Test the getX, getY functions.
    v = Vector(2,4)
    x = v.getX()
    y = v.getY()
    test(v==Vector(x,y))
 


