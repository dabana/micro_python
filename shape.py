from microbit import *
import math

class Shape(object):
    
    def __init__(self, shape):
        self._type = shape # an integer between 0 and 3 included
        self._orientation = 0 # an integer between 0 and 3 included
        self._x = 0 # index of control vertex
        self._y = 0 # index of control vertex
        self._vertices = []
        self.draw()
        
    def draw(self):
        self._updateVertices()
        for tup in self._vertices:
            switchOn(tup[0], tup[1])
    
    def _updateVertices(self):
    
        if self._type == 0: #dot
            self._x, self._y = selectCoordinates(0,4)
            v0 = (self._x, self._y)
            self._vertices = [v0]
        
        if self._type == 1: #two pixels line
            b, _, _, sn = binaryDecompositon(self._orientation)
            self._x, self._y = selectCoordinates(0 - sn * b, 4 - sn * b)
            v0 = (self._x, self._y)
            v1 = ((self.x + sn * b ) % 5, self.y + sn * (not b))
            self._vertices = [v0, v1]
        
        if self._type == 2: #three pixels l-shape
            b1, _, _, sn1 = binaryDecompositon(orientation)
            b2, _, _, sn2 = binaryDecompositon((orientation + 1) % 4)
            offset = sn1 * b1 + sn2 * b2
            l_offset = offset if offset < 0 else 0
            r_offset = offset if offset > 0 else 0
            self._x, self._y = selectCoordinates(0 - l_offset, 4 - r_offset)
            v0 = (self._x, self._y)
            v1 = ((self._x + sn1 * b1 ) % 5, self._y + sn1 * (not b1))
            v2 = ((self._x + sn2 * b2 ) % 5, self._y + sn2 * (not b2))
            self._vertices = [v0, v1, v2]
            
        if self._type == 3: #three pixels line
            b, _, _, sn = binaryDecompositon(self._orientation)
            self._x, self._y = selectCoordinates(0 + b, 4 - b)
            v0 = (self._x, self._y)
            v1 = ((self._x + sn * b ) % 5, self._y + sn * (not b))
            v2 = ((self._x - sn * b ) % 5, self._y - sn * (not b))
            self._vertices = [v0, v1, v2]
            
    def setOrientation(self, orientation):
        self._orientation = orientation
        self._updateVertices()
        
    def setPosition(self, x, y):
        self._x = x
        self._y = y
        self._updateVertices()
        
    def setType(self, shape_type):
        self._type = shape_type
        self._updateVertices()
            

def mapInteger(anInteger, from1, to1, from2, to2):
    span1 = math.fabs(to1 - from1 + 1)
    span2 = math.fabs(to2 - from2 + 1)
    scaling_factor = span1 / span2
    return int(from2 + math.floor(anInteger / scaling_factor))
    
def selectCoordinates(min_x, max_x):
    x_index = mapInteger(pin1.read_analog(),0,1023,0,4)
    x_index = max_x if x_index > (max_x - 1) else x_index
    x_index = min_x if x_index < min_x else x_index
    y_index = mapInteger(pin2.read_analog(),0,1023,0,4)
    coordinates = [x_index, y_index]
    return coordinates

def binaryDecompositon(integer):
    b1 = integer % 2 == 1
    b2 = (integer - 2) >= 0
    sn1 = 1 if b1 == 1 else -1
    sn2 = 1 if b2 == 1 else -1
    return [b1, b2, sn1, sn2]

def switchOn(x, y):
    if 0 <= y <= 4:
        display.set_pixel(x, y, 9)
        

            
            