'''
Created on 25 mar 2013

@author: Expert
'''
from model import Game_301
from model.player import Player
from tkinter import Tk, StringVar
from tkinter.constants import BOTH, TOP, LEFT
from tkinter.ttk import Label, Frame, Style, Button, Entry, OptionMenu

class SettingsUI:
    
    def __init__(self, mainFrame):
        "initiates settings and creates the interface"
        self.playerList = []
        self.gameList = ("301", "501", "Killer")
        self.initUI(mainFrame)
        
    
    def buildPlayerHeaderString(self):
        """Build a connection string from a dictionary of parameters.
    
        Returns string."""
        return "     ".join(["%s" % player.name for player in self.playerList])
    
    def addPlayer(self, name):
        self.playerList.append(Player(name))
    
    def initUI(self, mainFrame):
        """initialize the User Interface"""
        
        # styles
        style = Style()
        style.configure("TR.TLabel", background="#ACF059")
        style.configure("GRN.TFrame", background="#ACF059")
        style.configure("BLK.TFrame", background="black")
        
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
        nameFieldVar = StringVar()
        playerNameEntry = Entry(addPlayerFrame, textvariable = nameFieldVar)
        playerNameEntry.pack(side=LEFT)
        # create add player button
        addButton = Button(addPlayerFrame, text="Add player")
        addButton.pack(side=LEFT)
        
        # create choose game list
        currentGame = StringVar()
        currentGame.set(self.gameList[0])
        gameDropDown = OptionMenu(mainFrame, currentGame, self.gameList[0], *self.gameList)
        gameDropDown.pack(side=TOP)

        # create start game button
        startGameButton = Button(mainFrame, text="Start")
        def startGame(event):
            "TODO: Starts selected game"
            mainFrame.pack_forget()
            gameFrame = Frame(root)
            gameFrame.pack(fill=BOTH, expand=1)
            Game_301.Game301(gameFrame, self.playerList)
        
        startGameButton.bind("<Button-1>", startGame)
        startGameButton.pack(side=TOP)
        
        # create label and set text
        playerString = StringVar()
        playerString.set(self.buildPlayerHeaderString())
        headerLabel = Label(topFrame, textvariable=playerString, style="TR.TLabel")
        headerLabel.pack(side=TOP)
        
        #bind add player events
        def addPlayerCallback(event):
            "callback method for the add player button"
            name = playerNameEntry.get()
            self.addPlayer(name)
            playerString.set(self.buildPlayerHeaderString())
            nameFieldVar.set("")
             
        addButton.bind("<Button-1>", addPlayerCallback)
    
        
    
    
if __name__ == "__main__":
            # window size
    root = Tk()
    root.geometry("400x250")
    mainFrame = Frame(root)
    mainFrame.pack(fill=BOTH)
    SettingsUI(mainFrame)
    
    # show window
    root.mainloop()
    
