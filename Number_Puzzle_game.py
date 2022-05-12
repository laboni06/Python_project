from tkinter import*
import random
import tkinter.messagebox

root = Tk()
root.geometry("1350x760+0+0")
root.title("Number Puzzle Game")
root.configure(bg='Cadet blue')

rootFrame = Frame(root, bg='Cadet Blue', pady = 2, padx=40, width=1350, height=100, relief="solid")
rootFrame.grid(row=0, column=0)

lblTitle = Label(rootFrame, font=('arial', 80, 'bold'), text="Number Puzzle Game", bd=10, bg='Cadet blue', fg='black',
                 justify=CENTER, borderwidth=12,relief="solid",width=19)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg='Cadet blue', bd=10, width=1350, height=600, relief="solid")
MainFrame.grid(row=1, column=0, padx=30 )

ButtonFrame = LabelFrame(MainFrame, text="Number Puzzle", font=('arial', 12, 'bold'), fg='Cornsilk', bg='Cadet blue',
                         bd=10, width=700, height=500, relief="ridge")
ButtonFrame.pack(side=LEFT)

ScoreFrame = LabelFrame(MainFrame, text="Score Recorder", font=('arial', 12, 'bold'), fg='Cornsilk', bg='Cadet blue',
                        bd=10, padx=1, width=540, height=500, relief="ridge")
ScoreFrame.pack(side=RIGHT)

CountClickFrame = Frame(ScoreFrame, bg='Cadet blue', bd=10, padx=10, pady=2, width=540, height=190, relief="ridge")
CountClickFrame.grid(row=0, column=0)

WinnerFrame = Frame(ScoreFrame, bg='Cadet blue', bd=10, padx=10, pady=2, width=540, height=140, relief="ridge")
WinnerFrame.grid(row=1, column=0)

ResetExitFrame = Frame(ScoreFrame, bg='Cadet blue', bd=10, padx=10, pady=2, width=540, height=140, relief="ridge")
ResetExitFrame.grid(row=2, column=0)

clickCounter = 0
displayClicks = StringVar()
displayClicks.set("Total Clicks" + "\n" + "0")

gameStateString = StringVar()


def updateCounter():
    global clickCounter, displayClicks

    displayClicks.set("Total Clicks" + "\n" + str(clickCounter))


def gameStateUpdate(gameState):
    global gameStateString
    gameStateString.set(gameState)


class Button_:
    def __init__(self, text_, x, y):
        self.enterValue = text_
        self.txtIntake = StringVar()
        self.txtIntake.set(text_)
        self.x = x
        self.y = y
        self.btnNumber = Button(ButtonFrame, textvariable=self.txtIntake, font=('arial', 80), bd=5, borderwidth=4,
                                relief='solid', command=lambda i= self.x, j= self.y : emptySpotChecker(i, j))
        self.btnNumber.place(x=self.x*168, y=self.y*152, width=170, height=160)


def shuffle():
    global btnCheckers, clickCounter
    nums = []
    for x in range(12):
        x += 1
        if x == 12:
            nums.append("")
        else:
            nums.append(str(x))

    for y in range(len(btnCheckers)):
        for x in range(len(btnCheckers[y])):
            num = random.choice(nums)
            btnCheckers[y][x].txtIntake.set(num)
            nums.remove(num)

    clickCounter = 0
    updateCounter()
    gameStateUpdate("")


def iExit():
    iExit = tkinter.messagebox.askyesno("Number Puzzle", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return


lblCountClicks = Label(CountClickFrame, textvariable=displayClicks, borderwidth=4, relief="solid",
                       font=("Arial",40)).place(x=0, y=10, width=500, height=150)

lblWinner = Label(WinnerFrame, textvariable=gameStateString, borderwidth=4, relief="solid",
                  font=("Arial", 40)).place(x=0, y=10, width=500, height=100)

btnExit = Button(ResetExitFrame, text="Exit", font=("Arial", 40, "bold"), bd=5, borderwidth=4, relief='solid',
                 command=iExit).place(x=250, y=10, width=250, height=100)

btnReset = Button(ResetExitFrame, text="Reset", font=("Arial", 40, "bold"), bd=5, borderwidth=4, relief='solid',
                  command=shuffle).place(x=0, y=10, width=250, height=100)

btnCheckers = []

name = 0
for y in range(3):
    btnCheckers_ = []
    for x in range(4):
        name += 1
        if name == 12:
            name = ""
        btnCheckers_.append(Button_(str(name), x, y))
    btnCheckers.append(btnCheckers_)

shuffle()


def emptySpotChecker (y, x):
    global btnCheckers, clickCounter

    if not btnCheckers[x][y].txtIntake.get() == "":
        for i in range(-1, 2):
            newX = x+i
            if not (newX < 0 or len(btnCheckers)-1 < newX or i == 0):
                if btnCheckers[newX][y].txtIntake.get() == "":
                    text = btnCheckers[x][y].txtIntake.get()
                    btnCheckers[x][y].txtIntake.set(btnCheckers[newX][y].txtIntake.get())
                    btnCheckers[newX][y].txtIntake.set(text)
                    Checkwinner()
                    break
        for j in range(-1, 2):
            newY = y+j

            if not (newY < 0 or len(btnCheckers[0]) - 1 < newY or j == 0):
                if btnCheckers[x][newY].txtIntake.get() == "":
                    text = btnCheckers[x][y].txtIntake.get()
                    btnCheckers[x][y].txtIntake.set(btnCheckers[x][newY].txtIntake.get())
                    btnCheckers[x][newY].txtIntake.set(text)
                    Checkwinner()
                    break
        clickCounter += 1
        updateCounter()

def Checkwinner():
    lost = False
    for y in range(len(btnCheckers)):
        for x in range(len(btnCheckers[y])):
            if btnCheckers[y][x].enterValue != btnCheckers[y][x].txtIntake.get():
                lost = True
                break
    if not lost:
        gameStateUpdate("You are a Winner!")

root.mainloop()

