import random

class Domino:
    def __init__(self, value=-1, size=37, orientation="H", status=True):
        if (value < 0 or value > 77):
            self.randomize()
        else:
            self.val=value
        self.sze = size
        if (size < 30 and size > 100):
            size = 60
        self.ori = orientation
        if (orientation != "H" and orientation != "V"):
            orientation = "H"
        self.dia = self.sze // 5
        self.gap = self.dia // 2
        self.stt = status

    def __str__(self):
        return (str(self.val//10) + str(self.val%10))

    def getValue(self):
        self.val = objValue.get()
        return

    def setValue(self, value):
        self.val=value
        return

    def flip(self):
        Y = self.val % 10
        X = self.val // 10
        self.val = Y*10 + X
        return

    def setOrientation(self, orientation):
        self.ori = orientation
        return

    def setSize(self, size):
        self.sze = size
        self.dia = self.sze // 5
        self.gap = self.dia // 2

    def setFace(self, faceup):
        self.stt = faceup

    def randomize(self):
        self.val = random.randint(1, 6)*10 + random.randint(1, 6)

    def draw(self, canvas, x=0, y=0):
        self.drawHalf(canvas, x, y, self.val//10)
        if (self.ori=="H"):
            self.drawHalf(canvas, x+self.sze, y, self.val%10)
        else:
            self.drawHalf(canvas, x, y+self.sze, self.val%10)

    def shiftDraw(self, canvas, x=0, y=0):
        self.shiftDrawHalf(canvas, x, y, self.val//10)
        if (self.ori=="H"):
            self.shiftDrawHalf(canvas, x+self.sze, y, self.val%10)
        else:
            self.shiftDrawHalf(canvas, x, y+self.sze, self.val%10)

    def drawHalf(self, canvas, x, y, value):
        canvas.create_rectangle(x, y, x+self.sze, y+self.sze, width=1, outline="black", fill="white")
        if (self.stt == True):
            g = self.gap
            d = self.dia
            if (value == 1):
                canvas.create_oval(x+g+d+g, y+g+d+g, x+g+d+g+d, y+g+d+g+d, fill="black") #5
            elif (value==2 or value==3 or value==4 or value==5 or value==6):
                canvas.create_oval(x+g, y+g, x+g+d, y+g+d, fill="black") #1
                canvas.create_oval(x+g+d+g+d+g, y+g+d+g+d+g, x+g+d+g+d+g+d, y+g+d+g+d+g+d, fill="black") #9
                if (value==3 or value==5):
                    canvas.create_oval(x+g+d+g, y+g+d+g, x+g+d+g+d, y+g+d+g+d, fill="black") #5
                if (value==4 or value==5 or value==6):
                    canvas.create_oval(x+g+d+g+d+g, y+g, x+g+d+g+d+g+d, y+g+d, fill="black") #3
                    canvas.create_oval(x+g, y+g+d+g+d+g, x+g+d, y+g+d+g+d+g+d, fill="black") #7
                if (value==6):
                    canvas.create_oval(x+g+d+g, y+g, x+g+d+g+d, y+g+d, fill="black") #2
                    canvas.create_oval(x+g+d+g, y+g+d+g+d+g, x+g+d+g+d, y+g+d+g+d+g+d, fill="black") #8

    def shiftDrawHalf(self, canvas, x, y, value):
        const = 2
        canvas.create_rectangle(x, y, x+self.sze, y+self.sze, width=1, outline="black", fill="white")
        if (self.stt == True):
            g = self.gap
            d = self.dia
            if (value == 1):
                canvas.create_oval(x+g+d+g+const, y+g+d+g+const, x+g+d+g+d+const, y+g+d+g+d+const, fill="black") #5
            elif (value==2 or value==3 or value==4 or value==5 or value==6):
                canvas.create_oval(x+g+const, y+g+const, x+g+d+const, y+g+d+const, fill="black") #1
                canvas.create_oval(x+g+d+g+d+g+const, y+g+d+g+d+g+const, x+g+d+g+d+g+d+const, y+g+d+g+d+g+d+const, fill="black") #9
                if (value==3 or value==5):
                    canvas.create_oval(x+g+d+g+const, y+g+d+g+const, x+g+d+g+d+const, y+g+d+g+d+const, fill="black") #5
                if (value==4 or value==5 or value==6):
                    canvas.create_oval(x+g+d+g+d+g+const, y+g+const, x+g+d+g+d+g+d+const, y+g+d+const, fill="black") #3
                    canvas.create_oval(x+g+const, y+g+d+g+d+g+const, x+g+d+const, y+g+d+g+d+g+d+const, fill="black") #7
                if (value==6):
                    canvas.create_oval(x+g+d+g+const, y+g+const, x+g+d+g+d+const, y+g+d+const, fill="black") #2
                    canvas.create_oval(x+g+d+g+const, y+g+d+g+d+g+const, x+g+d+g+d+const, y+g+d+g+d+g+d+const, fill="black") #8  

    def __add__(self, domino):
        a1 = min(self.val // 10, self.val % 10)
        a2 = max(self.val // 10, self.val % 10)
        b1 = min(domino.val // 10, domino.val % 10)
        b2 = max(domino.val // 10, domino.val % 10)
        return ((a1*10+a2)+(b1*10+b2))

    def __sub__(self, domino):
        a1 = min(self.val // 10, self.val % 10)
        a2 = max(self.val // 10, self.val % 10)
        b1 = min(domino.val // 10, domino.val % 10)
        b2 = max(domino.val // 10, domino.val % 10)
        return ((a1*10+a2)-(b1*10+b2))

    def __mul__(self, domino):
        a1 = min(self.val // 10, self.val % 10)
        a2 = max(self.val // 10, self.val % 10)
        b1 = min(domino.val // 10, domino.val % 10)
        b2 = max(domino.val // 10, domino.val % 10)
        return ((a1*10+a2)*(b1*10+b2))

    def __gt__(self, domino):
        a1 = min(self.val // 10, self.val % 10)
        a2 = max(self.val // 10, self.val % 10)
        b1 = min(domino.val // 10, domino.val % 10)
        b2 = max(domino.val // 10, domino.val % 10)
        return ((a1*10+a2)>(b1*10+b2))

    def __ge__(self, domino):
        a1 = min(self.val // 10, self.val % 10)
        a2 = max(self.val // 10, self.val % 10)
        b1 = min(domino.val // 10, domino.val % 10)
        b2 = max(domino.val // 10, domino.val % 10)
        return ((a1*10+a2)>=(b1*10+b2))

    def __lt__(self, domino):
        a1 = min(self.val // 10, self.val % 10)
        a2 = max(self.val // 10, self.val % 10)
        b1 = min(domino.val // 10, domino.val % 10)
        b2 = max(domino.val // 10, domino.val % 10)
        return ((a1*10+a2)<(b1*10+b2))

    def __le__(self, domino):
        a1 = min(self.val // 10, self.val % 10)
        a2 = max(self.val // 10, self.val % 10)
        b1 = min(domino.val // 10, domino.val % 10)
        b2 = max(domino.val // 10, domino.val % 10)
        return ((a1*10+a2)<=(b1*10+b2))

    def __eq__(self, domino):
        a1 = min(self.val // 10, self.val % 10)
        a2 = max(self.val // 10, self.val % 10)
        b1 = min(domino.val // 10, domino.val % 10)
        b2 = max(domino.val // 10, domino.val % 10)
        return ((a1*10+a2)==(b1*10+b2))

    def __ne__(self, domino):
        a1 = min(self.val // 10, self.val % 10)
        a2 = max(self.val // 10, self.val % 10)
        b1 = min(domino.val // 10, domino.val % 10)
        b2 = max(domino.val // 10, domino.val % 10)
        return ((a1*10+a2)!=(b1*10+b2))