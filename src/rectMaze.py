'''
rectMaze.py

Created Jul, 2024

@author: mikejyg
'''
import ast

# rectangular maze.
class RectMaze():
    def __init__(self, width, height):
        if width<1 or height<1:
            raise Exception("width and height must be greater than 1.")
        self.width=width
        self.height=height
        
        self.graph=dict()
        
        for x in range(self.width):
            for y in range(self.height):
                conns=[]
                if x>0:
                    conns.append( (x-1,y) )
                if y>0:
                    conns.append( (x,y-1) )
                if x<self.width-1:
                    conns.append( (x+1,y) )
                if y<self.height-1:
                    conns.append( (x,y+1) )
                
                self.graph[(x,y)]=conns
                
    
    def printRepr(self):
        # print("width and height:")
        print(repr((self.width, self.height)))
        # print("nodes:")
        print(repr(self.graph))

    
    def save(self, f):
        f.write(repr((self.width, self.height)))
        f.write("\n")
        f.write(repr(self.graph))
        f.write("\n")
        
    def load(self, f):
        whStr=f.readline()
        wh=ast.literal_eval(whStr)
        self.width=wh[0]
        self.height=wh[1]
        gStr=f.readline()
        self.graph=ast.literal_eval(gStr)
