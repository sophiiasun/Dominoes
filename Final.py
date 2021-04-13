# Credits: ===============================================================
# Authors: Sophia Sun, Thomas Wang 
# Date: June 25, 2020
# Purpose: Dominoes Game with GUI Interface
# Note: Special Thanks to Mr. Smith of ICU3U1 at Milliken Mills High School
# ========================================================================

from tkinter import *
from Domino import Domino
from DominoHand import DominoHand
from DominoTable import DominoTable
from DominoGame import DominoGame
import random
import time

window = Tk()
window.resizable(0, 0)
window.config(padx=10, pady=10, bg="slateblue4")

# ============================= M E T H O D S =============================
# Disabled all the user command buttons until it reaches their turn
def disableAll():
    if (oGameOver.get() == 1):
        return
    placeB.config(state="disabled")
    dom1B.config(state="disabled")
    dom2B.config(state="disabled")
    dom3B.config(state="disabled")
    dom4B.config(state="disabled")
    dom5B.config(state="disabled")
    dom6B.config(state="disabled")
    dom7B.config(state="disabled")
    skipB.config(state="disabled")

# Enables/disables the domino choices accordingly to what the player can/cannot place down
def checkPlayerChoices():
    disableAll()
    oMessage.set("It's your turn!")
    if (oGameOver.get() == 1):
        return
    skipB.config(state="normal")
    if (GAMEBOARD.isPlaceable(GAMEBOARD.hands[0].list1[0].val) > 0):
        dom1B.config(state="normal")
    if (GAMEBOARD.isPlaceable(GAMEBOARD.hands[0].list1[1].val) > 0):
        dom2B.config(state="normal")
    if (GAMEBOARD.isPlaceable(GAMEBOARD.hands[0].list1[2].val) > 0):
        dom3B.config(state="normal")
    if (GAMEBOARD.isPlaceable(GAMEBOARD.hands[0].list1[3].val) > 0):
        dom4B.config(state="normal")
    if (GAMEBOARD.isPlaceable(GAMEBOARD.hands[0].list1[4].val) > 0):
        dom5B.config(state="normal")
    if (GAMEBOARD.isPlaceable(GAMEBOARD.hands[0].list1[5].val) > 0):
        dom6B.config(state="normal")
    if (GAMEBOARD.isPlaceable(GAMEBOARD.hands[0].list1[6].val) > 0):
        dom7B.config(state="normal")

# Player names show up on labels
def setNames():
    if (oGameOver.get() == 1):
        return
    oName0.set(GAMEBOARD.names[0] + " <-")
    oName1.set(GAMEBOARD.names[1] + " ^")
    oName2.set(GAMEBOARD.names[2] + " ->")
    oName3.set(GAMEBOARD.names[3] + " v")

# Stores the choice that the player has made
def playerClickButton(choice):
    if (oGameOver.get() == 1):
        return
    oPlayerChoice.set(choice)
    if (choice >= 0 and choice <= 6): # User chose a domino
        val = GAMEBOARD.hands[0].list1[choice].val
        oMessage.set("You selected " + str(val//10) + "|" + str(val%10) + ".")
    placeB.config(state="normal")

# Checks the winner of this round
def checkWinner():
    if (oGameOver.get() == 1):
        return
    if (GAMEBOARD.hands[0].valDomCnt == 0):
        disableAll()
        messagebox.showinfo(title="Congratulations!", message="You won this game! You're too good!!\nClick 'Start Game' for a new game.")
        oGameOver.set(1)
    elif(GAMEBOARD.hands[1].valDomCnt == 0 or GAMEBOARD.hands[2].valDomCnt == 0 or GAMEBOARD.hands[3].valDomCnt == 0):
        disableAll()
        messagebox.showinfo(title="Boohoohoo!", message="You lost this game! Try harder next time!\nClick 'Start Game' for a new game.")
        oGameOver.set(1)

# Starts the game off by placing the 66 domino first, regardless of who has it
def startGame(DC, LC, UC, RC, gameC):
    reset()
    GAMEBOARD.getNames()
    setNames()
    GAMEBOARD.deal() # Deal dominoes to each player
    window.update(); time.sleep(1.5)
    GAMEBOARD.drawDeal(0, DC)
    displayPlayerOptions()
    window.update(); time.sleep(0.7)
    GAMEBOARD.drawDeal(1, LC)
    window.update(); time.sleep(0.7)
    GAMEBOARD.drawDeal(2, UC)
    window.update(); time.sleep(0.7)
    GAMEBOARD.drawDeal(3, RC)
    window.update(); time.sleep(1.5)
    oSkipCounter.set(0)
##    time.sleep(1)
    p = GAMEBOARD.turn
    if (p == 0): # Player goes first
        oStartGame.set(1)
        dom7B.config(state="normal")
        oMessage.set("It's your turn!")
        window.update()
    else: # Comp goes first
        getCompFirstMove()

# Handles player button choices
def placeDown():
    if (oGameOver.get() == 1):
        return
    if(oPlayerChoice.get()==-1): # Check skip counter
        oSkipCounter.set(oSkipCounter.get() + 1)
        checkSkipCounter()
    else:
        oSkipCounter.set(0)
        val = GAMEBOARD.hands[0].list1[oPlayerChoice.get()].val
        opt = GAMEBOARD.isPlaceable(val)
        if (opt == 3 and oStartGame.get() == 0):
            tmp = messagebox.askquestion(title="Choice", message="That domino can be placed at both the front and the back! Click 'Yes' to place at the right/bottom and 'No' to place at the left/top.")
            opt = 1
            if (tmp == "no"):
                opt = 2
        elif (oStartGame.get() == 1):
            opt = 1
        if (opt == 1 and oStartGame.get()==1):
            GAMEBOARD.table.drawFirst()
            oStartGame.set(0)
            GAMEBOARD.coverDom(0, 6, playerDC)
            GAMEBOARD.hands[0].dropDomino(66)
        elif (opt == 1):
            GAMEBOARD.getUserMove(val, "F", playerDC)
        elif (opt == 2):
            GAMEBOARD.getUserMove(val, "B", playerDC)
        checkWinner()
    window.update()
    disableAll() # Disable all user controls after move has been made
    time.sleep(1)
    window.update()
    oPlayerChoice.set(-1)
    GAMEBOARD.turn = (GAMEBOARD.turn + 1) % 4
    getCompMove()
    window.update()

# Controls the movements for all 
def getCompMove():
    # Player 1
    if (oGameOver.get() == 1):
        return
    time.sleep(1)
    if (GAMEBOARD.turn == 1):
        getMove(1, playerLC)
    # Player 2
    if (GAMEBOARD.turn == 2):
        getMove(2, playerUC)
    # Player 3
    if (GAMEBOARD.turn == 3):
        getMove(3, playerRC)
        checkPlayerChoices()
    window.update()

# The comp with 6|6 piece places it down first
def getCompFirstMove():
    if (oGameOver.get() == 1):
        return
    oStartGame.set(0)
    move = 66
    player = GAMEBOARD.turn
    canvas = playerRC
    if (player == 1):
        canvas = playerLC
    elif (player == 2):
        canvas = playerUC
    oMessage.set(GAMEBOARD.names[player] + " has made a move!")
    oSkipCounter.set(0)
    checkWinner()
    checkSkipCounter()
    coords = GAMEBOARD.getCoords(player, move)
    GAMEBOARD.coverDom(player, GAMEBOARD.hands[player].findValue(move), canvas)
    GAMEBOARD.hands[player].dropDomino(move)
    GAMEBOARD.hands[player].valDomCnt = GAMEBOARD.hands[player].valDomCnt - 1
    GAMEBOARD.table.drawFirst()
    GAMEBOARD.turn = (GAMEBOARD.turn + 1) % 4
    window.update()
    if (GAMEBOARD.turn == 0):
        checkPlayerChoices()
    else:
        getCompMove()

# Gets individual player move
def getMove(player, canvas):
    if (oGameOver.get() == 1):
        return
    move = GAMEBOARD.getCompMove(player, canvas)
    if (move != -1):
        oMessage.set(GAMEBOARD.names[player] + " has made a move!")
        oSkipCounter.set(0)
    else:
        oMessage.set(GAMEBOARD.names[player] + " skips!")
        oSkipCounter.set(oSkipCounter.get() + 1)
    window.update()
    time.sleep(1)
    checkWinner()
    checkSkipCounter()
    GAMEBOARD.turn = (GAMEBOARD.turn + 1) % 4

# Displays domino options onto user control buttons
def displayPlayerOptions():
    tmpval = GAMEBOARD.hands[0].list1[0].val
    oDom1.set(str(tmpval//10) + "|" + str(tmpval%10))
    tmpval = GAMEBOARD.hands[0].list1[1].val
    oDom2.set(str(tmpval//10) + "|" + str(tmpval%10))
    tmpval = GAMEBOARD.hands[0].list1[2].val
    oDom3.set(str(tmpval//10) + "|" + str(tmpval%10))
    tmpval = GAMEBOARD.hands[0].list1[3].val
    oDom4.set(str(tmpval//10) + "|" + str(tmpval%10))
    tmpval = GAMEBOARD.hands[0].list1[4].val
    oDom5.set(str(tmpval//10) + "|" + str(tmpval%10))
    tmpval = GAMEBOARD.hands[0].list1[5].val
    oDom6.set(str(tmpval//10) + "|" + str(tmpval%10))
    tmpval = GAMEBOARD.hands[0].list1[6].val
    oDom7.set(str(tmpval//10) + "|" + str(tmpval%10))

# Checks if no other players can make another move
def checkSkipCounter():
    if (oSkipCounter.get() >= 4):
        disableAll()
        oGameOver.set(1)
        oMessage.set("Start a New Game!")
        messagebox.showinfo(title="End of Game", message="It's a tie! No player can make another move. Please start a new game.")

# ============================= O B J E C T S =============================
oMessage = StringVar()
oDom1 = StringVar()
oDom2 = StringVar()
oDom3 = StringVar()
oDom4 = StringVar()
oDom5 = StringVar()
oDom6 = StringVar()
oDom7 = StringVar()
oName0 = StringVar()
oName1 = StringVar()
oName2 = StringVar()
oName3 = StringVar()
oPlayerChoice = IntVar()
oSkipCounter = IntVar()
oStartGame = IntVar()
oGameOver = IntVar()
oMessage.set("Start a New Game!")
oDom1.set("")
oDom2.set("")
oDom3.set("")
oDom4.set("")
oDom5.set("")
oDom6.set("")
oDom7.set("")
oName0.set("")
oName1.set("")
oName2.set("")
oName3.set("")
oPlayerChoice.set(-1)
oSkipCounter.set(0)
oGameOver.set(0)
oStartGame.set(1)

# ============================= W I D G E T S =============================
#Create
title = Label(window, width=25, text=" ------- DOMINOES ------- ", font="Courier 40 bold", bg="seashell1")
label = Label(window, width=58, textvariable=oMessage, font="Courier 18", bg="seashell1")
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
playerLC = Canvas(window, width=97, height=357, relief="ridge", bg="seashell1")
playerRC = Canvas(window, width=97, height=357, relief="ridge", bg="seashell1")
playerUC = Canvas(window, width=637, height=57, relief="ridge", bg="seashell1")
playerDC = Canvas(window, width=637, height=57, relief="ridge", bg="seashell3")
gameBoardC = Canvas(window, width=637, height=357, relief="ridge", bg="mediumpurple4")
playerLL = Label(window, width=9, textvariable=oName1, font="Courier 13 bold", bg="seashell1")
playerUL = Label(window, width=9, textvariable=oName2, font="Courier 13 bold", bg="seashell1")
playerRL = Label(window, width=9, textvariable=oName3, font="Courier 13 bold", bg="seashell1")
playerDL = Label(window, width=9, textvariable=oName0, font="Courier 13 bold", bg="seashell1")
#Place
playerLC.grid(row=4, column=1, padx=(0, 10), pady=(0, 10))
playerUC.grid(row=3, column=2, columnspan=7, padx=(0, 10), pady=(0, 10))
playerRC.grid(row=4, column=9, pady=(0, 10)) 
playerDC.grid(row=5, column=2, columnspan=7, padx=(0, 10), pady=(0, 10))
gameBoardC.grid(row=4, column=2, columnspan=7, padx=(0, 10), pady=(0, 10))
playerRL.grid(row=3, column=9, pady=(0, 10)) 
playerUL.grid(row=3, column=1, padx=(0, 10), pady=(0, 10))
playerLL.grid(row=5, column=1, padx=(0, 10), pady=(0, 10))
playerDL.grid(row=5, column=9, pady=(0, 10)) 

# USER CONTROLS: ----------------------------------------------------------
#Create
skipB = Button(window, width=7, text="SKIP", font="Courier 15 bold", bg="lavenderblush2", state="disabled", anchor=CENTER, command=lambda:placeDown())
dom1B = Button(window, width=6, textvariable=oDom1, font="Courier 15", bg="lavenderblush3", state="disabled", anchor=CENTER, command=lambda:playerClickButton(0))
dom2B = Button(window, width=6, textvariable=oDom2, font="Courier 15", bg="lavenderblush3", state="disabled", anchor=CENTER, command=lambda:playerClickButton(1))
dom3B = Button(window, width=6, textvariable=oDom3, font="Courier 15", bg="lavenderblush3", state="disabled", anchor=CENTER, command=lambda:playerClickButton(2))
dom4B = Button(window, width=6, textvariable=oDom4, font="Courier 15", bg="lavenderblush3", state="disabled", anchor=CENTER, command=lambda:playerClickButton(3))
dom5B = Button(window, width=6, textvariable=oDom5, font="Courier 15", bg="lavenderblush3", state="disabled", anchor=CENTER, command=lambda:playerClickButton(4))
dom6B = Button(window, width=6, textvariable=oDom6, font="Courier 15", bg="lavenderblush3", state="disabled", anchor=CENTER, command=lambda:playerClickButton(5))
dom7B = Button(window, width=6, textvariable=oDom7, font="Courier 15", bg="lavenderblush3", state="disabled", anchor=CENTER, command=lambda:playerClickButton(6))
placeB = Button(window, width=7, text="PLACE", font="Courier 15 bold", bg="lavenderblush2", state="disabled", anchor=CENTER, command=lambda:placeDown())   
#Place
skipB.grid(row=6, column=1, padx=5, sticky=W)
dom1B.grid(row=6, column=2, sticky=W)
dom2B.grid(row=6, column=3, sticky=W)
dom3B.grid(row=6, column=4, sticky=W)
dom4B.grid(row=6, column=5, sticky=W)
dom5B.grid(row=6, column=6, sticky=W)
dom6B.grid(row=6, column=7, sticky=W)
dom7B.grid(row=6, column=8, sticky=W)
placeB.grid(row=6, column=9, padx=(5, 0), sticky=W)

# MENU BAR: ---------------------------------------------------------------
menuM = Menu(window)
menubar = Menu(menuM, tearoff=0)
menubar.add_command(label="New Game", command=lambda:startGame(playerDC, playerLC, playerUC, playerRC, gameBoardC))
menubar.add_command(label="Quit", command=lambda:window.destroy())
menuM.add_cascade(label="Menu", menu=menubar)
window.config(menu=menuM)

# GAME OBJECTS
GAMEBOARD = DominoGame(DominoHand(), DominoHand(), DominoHand(), DominoHand(), DominoTable(gameBoardC, 300, 155))

# RESET -------------------------------------------------------------------
def reset():
    gameBoardC.delete(ALL)
    playerDC.delete(ALL); playerRC.delete(ALL); playerUC.delete(ALL); playerLC.delete(ALL)
    oDom1.set(""); oDom2.set(""); oDom3.set(""); oDom4.set(""); oDom5.set(""); oDom6.set(""); oDom7.set("");
    oName0.set(""); oName1.set(""); oName2.set(""); oName3.set("")
    oMessage.set("Start a New Game!")
##    nGAMEBOARD = DominoGame(DominoHand(), DominoHand(), DominoHand(), DominoHand(), DominoTable(gameBoardC, 300, 155))
##    GAMEBOARD = nGAMEBOARD
    # reset GAMEBOARD
##    for i in range(4): # clear hand and cnt
##        GAMEBOARD.hands[i].list1 = []
##        GAMEBOARD.hands[i].valDomCnt == 0
##    GAMEBOARD.table.
    GAMEBOARD.hands = [DominoHand(), DominoHand(), DominoHand(), DominoHand()]
    GAMEBOARD.table = DominoTable(gameBoardC, 300, 155)
    GAMEBOARD.names = []
    GAMEBOARD.turn = -1
    #----------------
    oGameOver.set(0)
    oStartGame.set(0)
    time.sleep(1)
    window.update()