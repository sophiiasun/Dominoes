# Credits: ===============================================================
# Authors: Sophia Sun, Thomas Wang 
# Date: June 25, 2020
# Purpose: Dominoes Game with GUI Interface
# Note: Special Thanks to Mr. Smith of ICU3U1 at Milliken Mills High School
# ========================================================================

from tkinter import *
from Domino import *
import random

class DominoHand:
    def __init__ (self,size=0):
        self.size=size
        self.list1=[]
        self.valDomCnt = 7
                  
    def __str__ (self):
        tempstr="["
        for counter in range (self.size-1):
            tempstr+=str(self.list1[counter].val//10)
            tempstr+="|"
            tempstr+=str(self.list1[counter].val%10)
            tempstr+=", "
        if(self.size!=0):
            tempstr+=str(self.list1[self.size-1].val//10)
            tempstr+="|"
            tempstr+=str(self.list1[self.size-1].val%10)
        tempstr+="] size: " + str(self.size)
        return tempstr
 
    def displayHand(self,canvas,x=0,y=0, rotation = "H"): #rotations (horizontal = "H", vertical = "V")
        if(rotation == "H"):
            self.setOrientation("H")
            xsize=x
            ysize=y
            for counter in range (self.size):
                self.list1[counter].draw(canvas,xsize,ysize)
                xsize+=2*self.list1[counter].sze+30
                if(counter%3==2):
                    ysize+=self.list1[counter].sze+30
                    xsize=x
        else:
            self.setOrientation("V")
            xsize = x
            ysize = y
            for counter in range (self.size):
                self.list1[counter].draw(canvas,xsize,ysize)
                ysize+=2*self.list1[counter].sze+30
                if(counter%3==2):
                    xsize+=self.list1[counter].sze+30
                    ysize=y
      
    def setSize(self,size):
        for counter in range (self.size):
            self.list1[counter].setSize(size)

    def addDomino(self, tmpVal):
        tempDomino = Domino(tmpVal)
        self.list1.append(tempDomino)
        self.size+=1

    def valueOfDomino(self, index = 0):
        if(str(index).isdigit() and index < self.size):
            return self.list1[index].val
        else:
            print("ERROR, no such index exists")

    def setOrientation(self, orient = "H"):
        if(orient == "H" or orient =="V"):
            for counter in range (self.size):
                self.list1[counter].ori = orient

    def setFaceUp(self, faceUp = True): #faceup = true facedown = false
        if(str(faceUp).isdigit()):
            for counter in range (self.size):
                self.list1[counter].stt = faceUp

    def findValue(self, tmpVal):
        intPos=100
        for counter in range(0, self.size):
            if(self.list1[counter].val==tmpVal):
                intPos=min(intPos,counter)
        if(intPos==100):
            intPos=-1
        return intPos # returns -1 if not found

    def dropDomino(self, tmpVal):
        index = self.findValue(tmpVal)
        if(index != -1):
            self.list1[index].setValue(77)
            
    def sortHand (self):
        pointer1 = 0
        while(pointer1<len(self.list1)-1):
            if(self.list1[pointer1]>self.list1[pointer1+1]):
                self.list1[pointer1] , self.list1[pointer1+1] = self.list1[pointer1+1] , self.list1[pointer1]
                pointer1=0
            else:
                pointer1+=1