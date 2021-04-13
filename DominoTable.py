# ============================= C R E D I T S =============================
# Authors: Sophia Sun, Thomas Wang 
# Date: June 25, 2020
# Purpose: Dominoes Game with GUI Interface
# Note: Special Thanks to Mr. Smith of ICU3U1 at Milliken Mills High School
# =========================================================================

from DominoHand import *
from Domino import *

class DominoTable :
    def __init__ (self, canvas, x = 0, y = 0): #x,y is mididle of canvas
        self.list1 = [] #auto starts with 66 so don't append it into the list just drop it out maxwidth = 620
        self.start = 6 #startvalue
        self.end = 6 #end value
        self.x = x #x coord to start
        self.y = y #ycoord to start
        self.canvas = canvas #canvas
        self.frontRows = 0 #rows appended to front
        self.backRows = 0 #rows appended to back 
        self.xLength1 = x #x axis of the front
        self.xLength2 = x # x axis of the back
        self.yLength1 = y # y axis of the front
        self.yLength2 = y # y axis of the back      

    def drawFirst(self): #draws the 66 domino
        tempDomino = Domino(66)
        tempDomino.shiftDraw(self.canvas,self.x,self.y)

    def eraseDomino(self, canvas, x, y):
        canvas.delete(x, y)
    
    def addToTable(self, val, pos = "F"): #F to add to front B for back 
        right = 530; left = 0; size1 = 74; size2 = size1/2    
        tempDomino = Domino(val)
        if(pos=="B"):
            if(tempDomino.val//10==self.end):
                self.end = tempDomino.val%10
                if(self.backRows%2==1):
                    tempDomino.flip()
            else:
                self.end = tempDomino.val//10
                if(self.backRows%2==0):
                    tempDomino.flip()
            if(self.backRows%2==0):
                if(self.xLength2+size1<=right):
                    self.xLength2+=size1
                    tempDomino.shiftDraw(self.canvas,self.xLength2,self.yLength2)
                else:
                    self.xLength2+=size2
                    self.yLength2-=size1
                    tempDomino.setOrientation("V")
                    tempDomino.flip()
                    tempDomino.shiftDraw(self.canvas,self.xLength2,self.yLength2)
                    self.backRows+=1
            else:
                if(self.xLength2-size1>=left):
                    self.xLength2-=size1
                    tempDomino.shiftDraw(self.canvas,self.xLength2,self.yLength2)
                else:
                    self.yLength2-=size1 #80, 40 
                    tempDomino.setOrientation("V")
                    tempDomino.shiftDraw(self.canvas,self.xLength2,self.yLength2)
                    self.backRows+=1
                    self.xLength2-=size2 #make it so that the new row spawns dominos at the right spot
            self.list1.append(tempDomino)
                
        else:
            if(tempDomino.val//10==self.start):
                self.start = tempDomino.val%10
                if(self.frontRows%2==0):
                    tempDomino.flip()
            else:
                self.start= tempDomino.val//10
                if(self.frontRows%2==1):
                    tempDomino.flip()
                
            if(self.frontRows%2==0):
                if(self.xLength1-3*size2>=left):
                    self.xLength1-=size1
                    tempDomino.shiftDraw(self.canvas,self.xLength1,self.yLength1)
                else:
                    self.xLength1-=size2
                    tempDomino.setOrientation("V")
                    tempDomino.flip()
                    tempDomino.shiftDraw(self.canvas,self.xLength1,self.yLength1)
                    self.yLength1+=size1
                    self.frontRows+=1
                    self.xLength1-=size1 #make it so that the new row spawns dominos at the right spot
            else:
                if(self.xLength1+3*size2<=right):
                    self.xLength1+=size1
                    tempDomino.shiftDraw(self.canvas,self.xLength1,self.yLength1)
                else:
                    self.xLength1+=size1
                    tempDomino.setOrientation("V")
                    tempDomino.shiftDraw(self.canvas,self.xLength1,self.yLength1)
                    self.yLength1+= size1
                    self.frontRows+=1
                    self.xLength1+=size2 #make it so that the new row spawns dominos at the right spot
                    
            self.list1.insert(0,tempDomino)