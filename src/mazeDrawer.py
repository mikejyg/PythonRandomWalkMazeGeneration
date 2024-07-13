'''
mazeDrawer.py

Created Jul, 2024

@author: mikejyg
'''
import turtle

class MazeDrawer:
    margin=5
    
    def __init__(self, scale=20):
        self.scale=scale    # scale is the width and height of each maze cell.
        self.base=scale/2
        self.t=None
        
    def _toCellCenter(self, p):
        return (p[0]*self.scale + self.base + self.xoffset, p[1]*self.scale + self.base + self.yoffset)
    

    # draw node at the current position.
    # pen state should be up.
    def _drawNode(self):
        psave=self.t.pos()
        
        self.t.right(90)
        self.t.fd(self.nodeR)
        self.t.left(90)
        
        self.t.pd()
        self.t.begin_fill()
        self.t.circle(self.nodeR)
        self.t.end_fill()
        self.t.pu()
        
        self.t.setpos(psave)
    
    
    def _initTurtle(self, g):
        # do not re-init turtle
        if self.t:
            return
        
        # with added margin of 5 pixels.
        self.xoffset = - g.width * self.scale/2
        self.yoffset = - g.height * self.scale/2
    
        turtle.setup( g.width*self.scale + 2*MazeDrawer.margin, g.height*self.scale + 2*MazeDrawer.margin )
        self.t=turtle.Turtle()
        
    
    def drawPathsSet(self, g, paths, wait=True, drawNode=True):
        self._initTurtle(g)
        turtle.Screen().tracer(False)
        
        self.t.pensize(self.base)
        self.t.pencolor('gray')
        self.nodeR=self.base/3
        
        for nId in g.graph:
            for c in g.graph[nId]:
                if (nId, c) in paths:
                    # print(nId, c.nodeId)
                    n1=nId
                    n2=c
                    
                    self.t.pu()
                    self.t.goto( self._toCellCenter(n1) )
                    if drawNode:
                        self._drawNode()
                    self.t.pd()
                    self.t.goto( self._toCellCenter(n2) )
    
        self.t.pu()
        self.t.home()
        self.t.hideturtle()
        turtle.Screen().update()
        
        if wait:
            turtle.Screen().exitonclick()


    def _drawEastWall(self, nId):
        self.t.pu()
        self.t.goto( (nId[0]+1)*self.scale + self.xoffset, nId[1]*self.scale + self.yoffset )
        self.t.pd()
        self.t.goto( (nId[0]+1)*self.scale + self.xoffset, (nId[1]+1)*self.scale + self.yoffset )
        
        
    def _drawNorthWall(self, nId):
        self.t.pu()
        self.t.goto( (nId[0])*self.scale + self.xoffset, (nId[1]+1)*self.scale + self.yoffset )
        self.t.pd()
        self.t.goto( (nId[0]+1)*self.scale + self.xoffset, (nId[1]+1)*self.scale + self.yoffset )
        
        
    def _drawWestWall(self, nId):
        self.t.pu()
        self.t.goto( (nId[0])*self.scale + self.xoffset, (nId[1])*self.scale + self.yoffset )
        self.t.pd()
        self.t.goto( (nId[0])*self.scale + self.xoffset, (nId[1]+1)*self.scale + self.yoffset )
        
        
    def _drawSouthWall(self, nId):
        self.t.pu()
        self.t.goto( (nId[0])*self.scale + self.xoffset, (nId[1])*self.scale + self.yoffset )
        self.t.pd()
        self.t.goto( (nId[0]+1)*self.scale + self.xoffset, (nId[1])*self.scale + self.yoffset )
        

    def _skipFd(self, a):
        self.t.pu()
        self.t.fd(a)
        self.t.pd()

    def drawWalls(self, g, paths, wait=True):
        self._initTurtle(g)
        turtle.Screen().tracer(False)
        
        self.t.pensize(3)
        self.t.pencolor('gray')

        # draw boundary walls.
        self.t.pu()
        # turtle is at home, go to the upper-right corner.
        self.t.goto( g.width/2*self.scale, g.height/2*self.scale )
        self.t.right(90)
        self._skipFd(self.scale)
        self.t.fd(g.height*self.scale - self.scale * 2)
        self._skipFd(self.scale)
        
        self.t.right(90)
        self._skipFd(self.scale)
        self.t.fd(g.width*self.scale - self.scale * 2)
        self._skipFd(self.scale)

        self.t.right(90)
        self._skipFd(self.scale)
        self.t.fd(g.height*self.scale - self.scale * 2)
        self._skipFd(self.scale)

        self.t.right(90)
        self._skipFd(self.scale)
        self.t.fd(g.width*self.scale - self.scale * 2)
        # self._skipFd(self.scale)
        
        for nId in g.graph:
            for c in g.graph[nId]:
                if (nId, c) not in paths:
                    if c[0]>nId[0]:
                        self._drawEastWall(nId)
                    elif c[1]>nId[1]:
                        self._drawNorthWall(nId)
                    elif c[0]<nId[0]:
                        self._drawWestWall(nId)
                    elif c[1]<nId[1]:
                        self._drawSouthWall(nId)
                    else:
                        raise Exception("illegal connection:", nId, c)
                
        self.t.pu()
        self.t.home()
        self.t.hideturtle()
        turtle.Screen().update()
        
        if wait:
            turtle.Screen().exitonclick()


    def drawPaths(self, g, nodes, wait=True):
        self._initTurtle(g)
        turtle.Screen().tracer(False)
        
        self.t.pensize(self.base/2)
        self.t.pencolor('gray')

        firstNode=True        
        for n in nodes:
            if firstNode:
                self.t.pu()
                self.t.goto( self._toCellCenter(n) )
                self.t.pd()
                firstNode=False
            else:
                self.t.goto( self._toCellCenter(n) )
    
        self.t.pu()
        self.t.home()
        self.t.hideturtle()
        turtle.Screen().update()
        
        if wait:
            turtle.Screen().exitonclick()
