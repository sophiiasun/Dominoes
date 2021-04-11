#Author: Thomas Wang
#Date: May 5th 2020
#Purpose: To Develop the beginnings of the Domino class for future use
#-=-=-==-=-=-==-=--==-=-=-=--==--==-=-=-=--==-=-=--=-=-=-=-=-=--=-=-=-=-=-=

from tkinter import *
from Domino import Domino
from DominoHand import DominoHand
from DominoTable import DominoTable
from DominoGame import DominoGame
import random

window = Tk()
window.resizable(0, 0)
window.config(padx=10, pady=10, bg="slateblue4")

# ============================= M E T H O D S =============================
###Process during in-Game
##def inGame():
##    while (GAMEBOARD.hand[0].size > 0 and GAMEBOARD.hand[1].size > 0 and GAMEBOARD.hand[2].size > 0 and GAMEBOARD.hand[3].size > 0):
##        p = GAMEBOARD.turn
##        if (p > 0): # Comp turn
##            GAMEBOARD.getCompMove(p)
##        else: # Player turn
##            
##        GAMEBOARD.turn = (p + 1) % 4
##
### Enables/disables the domino choices accordingly to what the player can/cannot place down
##def checkPlayerChoices():
##    if (GAMEBOARD.hands[0][0] // 10):
##        
##
### Checks the winner of this round
##def checkWinner():
##    if (GAMEBOARD.hand[0].size == 0):
##        messagebox.showinfo(title="Congratulations!", message="You won this game! You're too good!!\nClick 'Start Game' for a new game.")
##    else:
##        messagebox.showinfo(title="Boohoohoo!", message="You lost this game! Try harder next time!\nClick 'Start Game' for a new game.")
##
##def startGame():
##    GAMEBOARD.deal() # Deal dominoes to each player
##    p = GAMEBOARD.turn
##    if (p == 0):
##        dom7B.config(state="normal")
##    else: # Comp goes first
##        GAMEBOARD.hands[p].dropDomino(66)
##        GAMEBOARD.table.addToTable(Domino(66))
##        
##    inGame()

# ============================= O B J E C T S =============================
oMessage = StringVar()
oDom1 = StringVar()
oDom2 = StringVar()
oDom3 = StringVar()
oDom4 = StringVar()
oDom5 = StringVar()
oDom6 = StringVar()
oDom7 = StringVar()
oMessage.set("Start a New Game!")
oDom1.set("")
oDom2.set("")
oDom3.set("")
oDom4.set("")
oDom5.set("")
oDom6.set("")
oDom7.set("")

# ============================= W I D G E T S =============================

#Create
title = Label(window, text=" ------- DOMINOES ------- ", font="Courier 40 bold", bg="seashell1")
label = Label(window, width=59, textvariable=oMessage, font="Courier 18", bg="seashell1")
#Place
title.grid(row=1, column=1, columnspan=9, pady=(0, 10))
label.grid(row=2, column=1, columnspan=9, pady=(0, 10))

# GAME BOARD: -------------------------------------------------------------

# Domino size: 20 by 40
# Domino gap: 5
# Width of U and D LFs: 620
# Height of U and D LFs: 45
# Width of L and R LFs: 85
# Height of L and R LFs: 340

#Create
playerLC = Canvas(window, width=85, height=340, relief="ridge", bg="seashell1")
playerRC = Canvas(window, width=85, height=340, relief="ridge", bg="seashell1")
playerUC = Canvas(window, width=620, height=45, relief="ridge", bg="seashell1")
playerDC = Canvas(window, width=620, height=45, relief="ridge", bg="seashell3")
gameBoardC = Canvas(window, width=620, height=340, relief="ridge", bg="mediumpurple4")
#Place
playerLC.grid(row=4, column=1, padx=(0, 10), pady=(0, 10))
playerUC.grid(row=3, column=2, columnspan=7, padx=(0, 10), pady=(0, 10))
playerRC.grid(row=4, column=9, pady=(0, 10))
playerDC.grid(row=5, column=2, columnspan=7, padx=(0, 10), pady=(0, 10))
gameBoardC.grid(row=4, column=2, columnspan=7, padx=(0, 10), pady=(0, 10))

# USER CONTROLS: ----------------------------------------------------------

#Create
skipB = Button(window, width=6, text="SKIP", font="Courier 15 bold", bg="lavenderblush2", state="disabled")
dom1B = Button(window, width=6, textvariable=oDom1, font="Courier 15", bg="lavenderblush3", state="disabled")
dom2B = Button(window, width=6, textvariable=oDom2, font="Courier 15", bg="lavenderblush3", state="disabled")
dom3B = Button(window, width=6, textvariable=oDom3, font="Courier 15", bg="lavenderblush3", state="disabled")
dom4B = Button(window, width=6, textvariable=oDom4, font="Courier 15", bg="lavenderblush3", state="disabled")
dom5B = Button(window, width=6, textvariable=oDom5, font="Courier 15", bg="lavenderblush3", state="disabled")
dom6B = Button(window, width=6, textvariable=oDom6, font="Courier 15", bg="lavenderblush3", state="disabled")
dom7B = Button(window, width=6, textvariable=oDom7, font="Courier 15", bg="lavenderblush3", state="disabled")
placeB = Button(window, width=6, text="PLACE", font="Courier 15 bold", bg="lavenderblush2", state="disabled")
#Place
skipB.grid(row=6, column=1)
dom1B.grid(row=6, column=2)
dom2B.grid(row=6, column=3)
dom3B.grid(row=6, column=4)
dom4B.grid(row=6, column=5)
dom5B.grid(row=6, column=6)
dom6B.grid(row=6, column=7)
dom7B.grid(row=6, column=8)
placeB.grid(row=6, column=9)

# GAME OBJECTS
GAMEBOARD = DominoGame(DominoHand(), DominoHand(), DominoHand(), DominoHand(), DominoTable(gameBoardC, 330, 270))