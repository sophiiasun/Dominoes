# ============================= C R E D I T S =============================
# Authors: Sophia Sun, Thomas Wang 
# Date: June 25, 2020
# Purpose: Dominoes Game with GUI Interface
# Note: Special Thanks to Mr. Smith of ICU3U1 at Milliken Mills High School
# =========================================================================

import random
import DominoTable
import DominoHand
import Domino
import time

class DominoGame: # table includes canvas used and start pos of domino snake
    def __init__(self, hand1, hand2, hand3, hand4, table):
        self.hands = []
        self.hands.append(hand1)
        self.hands.append(hand2)
        self.hands.append(hand3)
        self.hands.append(hand4)
        self.table = table
        self.NAMES = ["Aneesh", "Humpy", "Thotmas", "Robino", "Christ", "Flix", "Sophia", "Eason", "AsyA"]
        self.names = []
        self.turn = -1

    def getNames(self):
        self.names.append("YOU")
        taken = ""  
        for i in range(3):
            num = random.randint(0, 8)
            while (str(num) in taken):
                num = random.randint(0, 8)  
            taken += str(num)
            self.names.append(self.NAMES[num])

    def deal(self):
        doms = [0, 1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 22, 23, 24, 25, 26, 33, 34, 35, 36, 44, 45, 46, 55, 56, 66]
        for i in range(7): 
            for j in range(4): 
                rng = random.randint(0, len(doms)-1)
                if(doms[rng] == 66):
                    self.turn = j
                self.hands[j].addDomino(doms[rng])
                del doms[rng]
        for i in range (4):
            self.hands[i].sortHand()

    def drawDeal(self, player, canvas):
        x = 10
        y = 10
        if (player == 0 or player == 2):
            for dom in self.hands[player].list1:
                dom.setSize(40)
                dom.draw(canvas, x, y)
                x += dom.sze*2 + 10
        else:
            for dom in self.hands[player].list1:
                dom.setSize(40)
                dom.draw(canvas, x, y)
                y += dom.sze + 10

    def getCoords(self, player, val):
        index = self.hands[player].findValue(val)
        x = 10
        y = 10
        if (player == 0 or player == 2):
            for i in range(index):
                y += 50
        else:
            for i in range(index):
                x += 90
        return [50, 90]
            
    def canMove(self, player):
        for dom in self.hands[player].list1:
            if (dom.val // 10 == self.table.end or dom.val % 10 == self.table.end or dom.val // 10 == self.table.start or dom.val % 10 == self.table.start):
                return dom.val
        return -1

    def getUserMove(self, move, pos, canvas):
        if(pos =="F"):
            self.table.addToTable(move,"F")
        else:
            self.table.addToTable(move,"B")
        pos = self.hands[0].findValue(move)
        self.coverDom(0, pos, canvas)
        self.hands[0].dropDomino(move)
        self.hands[0].valDomCnt = self.hands[0].valDomCnt - 1

    def isPlaceable(self, domVal):
        placeFront = False
        placeBack = False
        if(domVal//10 == self.table.start or domVal%10 == self.table.start):
            placeFront = True
        if(domVal//10 == self.table.end or domVal%10 == self.table.end):
            placeBack = True
        if(placeFront == True and placeBack == True):
            return 3
        elif(placeBack == True):
            return 2
        elif(placeFront == True):
            return 1
        return 0

    def coverDom(self, player, index, canvas):
        x = 10
        y = 10
        if (player==0 or player==2):
            for i in range(index):
                x+=90
        else:
            for i in range(index):
                y+=50
        if (player==0 or player==2):    
            canvas.create_rectangle(x, y, x+80, y+40, fill="seashell3")
        else:
            canvas.create_rectangle(x, y, x+80, y+40, fill="seashell3")

    def getCompMove(self, player, canvas):
        move = self.canMove(player)
        if (move >= 0):
            coords = self.getCoords(player, move)
            self.coverDom(player, self.hands[player].findValue(move), canvas)
            self.hands[player].dropDomino(move)
            self.hands[player].valDomCnt = self.hands[player].valDomCnt - 1
            if(move // 10 == self.table.start or move % 10 == self.table.start):
                self.table.addToTable(move,"F")
            else:
                self.table.addToTable(move,"B")
            return move
        return -1