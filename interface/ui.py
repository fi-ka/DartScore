'''
Created on 25 mar 2013

@author: Expert
'''
from model import gameX01, gameClock
from model.player import Player
from tkinter import Tk, StringVar
from tkinter.constants import BOTH, TOP, LEFT
from tkinter.ttk import Label, Frame, Style, Button, Entry, OptionMenu

class SettingsUI:
    
    def __init__(self, mainFrame):
        "initiates settings and creates the interface"
        self.playerList = []
        self.gameList = ("301", "501", "Clock")
        self.initUI(mainFrame)
        
    
    def buildPlayerHeaderString(self):
        """Build a connection string from a dictionary of parameters.
    
        Returns string."""
        return "Players: " + ", ".join(["%s" % player.name for player in self.playerList])
    
    def addPlayerText(self, name):
        self.playerList.append(Player(name))
        
        #bind add player click event
    def onAddPlayerClick(self, event):
        "callback method for the add player button"
        self.addPlayer()
    
    def onAddPlayerEnter(self, event):
        "callback method for the add player button"
        if event.keycode == 13:
            self.addPlayer()
            
    def addPlayer(self):
        name = self.playerNameEntry.get()
        if name:
            self.addPlayerText(name)
            self.playerString.set(self.buildPlayerHeaderString())
            self.nameFieldVar.set("")
            self.playerNameEntry.focus()
        return("break")
     
    def initUI(self, mainFrame):
        """initialize the User Interface"""
        
        # styles
        style = Style()
        style.configure("GRN.TLabel", background="#ACF059")
        style.configure("GRN.TFrame", background="#ACF059")
        style.configure("BLK.TFrame", background="#595959")
        
        
        # create top frame
        topFrame = Frame(mainFrame, style="GRN.TFrame", padding=8)
        topFrame.pack(fill=BOTH, side=TOP)
        
        # create black border
        borderFrame = Frame(mainFrame, style="BLK.TFrame")
        borderFrame.pack(fill=BOTH, side=TOP)
        
        # create add player frame
        addPlayerFrame = Frame(mainFrame, padding=8)
        addPlayerFrame.pack(side=TOP)
        
        # create text field for add button
        self.nameFieldVar = StringVar()
        self.playerNameEntry = Entry(addPlayerFrame, textvariable = self.nameFieldVar)
        self.playerNameEntry.pack(side=LEFT)
        # create add player button
        addButton = Button(addPlayerFrame, text="Add player")
        addButton.pack(side=LEFT)
        
        # create choose game list
        self.currentGame = StringVar()
        self.currentGame.set(self.gameList[0])
        gameDropDown = OptionMenu(mainFrame, self.currentGame, self.gameList[0], *self.gameList)
        gameDropDown.pack(side=TOP)

        # create start game button
        startGameButton = Button(mainFrame, text="Start")
        
        startGameButton.bind("<Button-1>", self.startGame)
        startGameButton.pack(side=TOP)
        
        # create label and set text
        self.playerString = StringVar()
        self.playerString.set(self.buildPlayerHeaderString())
        headerLabel = Label(topFrame, textvariable=self.playerString, style="GRN.TLabel")
        headerLabel.pack(side=TOP)     
        addButton.bind("<Button-1>", self.onAddPlayerClick)
        self.playerNameEntry.bind("<Key>", self.onAddPlayerEnter)
        
        #set focus
        self.playerNameEntry.focus()
        
    def startGame(self,event):
        "starts the selected game"
        if self.playerList:
            mainFrame.pack_forget()
            gameFrame = Frame(root)
            gameFrame.pack(fill=BOTH, expand=1)
                
            game = self.currentGame.get()
            if game == "301":
                gameX01.GameX01(gameFrame, self.playerList)
            elif game == "501":                    
                gameX01.GameX01(gameFrame, self.playerList, 501)
            elif game == "Clock":
                gameClock.GameClock(gameFrame, self.playerList)
            else:
                gameX01.GameX01(gameFrame, self.playerList)
        
if __name__ == "__main__":
    
    # window size
    root = Tk()
    root.title("Dart Score")
    root.geometry("400x250")
    mainFrame = Frame(root)
    mainFrame.pack(fill=BOTH)
    SettingsUI(mainFrame)
    
    # show window
    root.mainloop()
    
