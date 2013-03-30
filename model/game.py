'''
Created on 29 mar 2013

@author: Expert
'''
from tkinter import StringVar
from tkinter.constants import BOTH, LEFT, TOP, BOTTOM, X
from tkinter.font import Font
from tkinter.ttk import Frame, Style, Label, Entry, Button

class Game():
    '''
    classdocs
    '''
    def setStyles(self):
        # styles
        style = Style()
        
        style.configure("WHT.TFrame", background="white")
        style.configure("WHT.TLabel", background="white")
        style.configure("GRAY.TFrame", background="#EEF5EB")
        style.configure("GRAY.TLabel", background="#EEF5EB")
        
        self.styleGrayFrame = "GRAY.TFrame"
        self.styleGrayLabel = "GRAY.TLabel"
        self.styleWhiteFrame = "WHT.TFrame"
        self.styleWhiteLabel = "WHT.TLabel"
        
        self.customFont = Font(family="Arial", size=9)
    
    def addRoundFrame(self, gameFrame):
        "adds the left round frame"
        # create round frame 
        self.roundFrame = Frame(gameFrame, style="WHT.TFrame")
        self.roundFrame.pack(side=LEFT, fill=BOTH)
        
        # create top frame
        headerFrame = Frame(self.roundFrame, style="GRN.TFrame", padding=8)
        headerFrame.pack(fill=BOTH, side=TOP)
        roundLabel = Label(headerFrame, text="", style="GRN.TLabel", font=self.customFont)
        roundLabel.pack(side=BOTTOM)
        
        # create black border
        borderFrame = Frame(self.roundFrame, style="BLK.TFrame")
        borderFrame.pack(fill=BOTH, side=TOP)
        
    def addPlayerFrame(self, gameFrame, player):
        "adds a player column to the interface"

        # create player frame 
        playerFrame = Frame(gameFrame, style="WHT.TFrame")
        self.playerFrameList.append(playerFrame)
        playerFrame.pack(side=LEFT, fill=BOTH, expand=1)
        
        # create top frame
        headerFrame = Frame(playerFrame, style="GRN.TFrame", padding=8)
        headerFrame.pack(fill=BOTH, side=TOP)
        nameLabel = Label(headerFrame, text="%s = %d" % (player.name, self.playerTotalScoreDict[player]), style="GRN.TLabel", font=self.customFont)
        nameLabel.pack(side=BOTTOM)
        
        # create black border
        borderFrame = Frame(playerFrame, style="BLK.TFrame")
        borderFrame.pack(fill=BOTH, side=TOP)
    
    def addSetScoreFrame(self, gameFrame):
        scoreFrame = Frame(gameFrame, style = "GRAY.TFrame")
        scoreFrame.pack(side=BOTTOM, fill=X)
        
        # create border
        borderFrame = Frame(scoreFrame, style = "BLK.TFrame")
        borderFrame.pack(side=TOP, fill=X)
        
        # create add score text field
        fieldButtonFrame = Frame(scoreFrame)
        fieldButtonFrame.pack(side=BOTTOM)
        
        # create score entry
        self.scoreVar = StringVar()
        scoreEntry = Entry(fieldButtonFrame, textvariable = self.scoreVar)
        scoreEntry.pack(side=LEFT)
        
        # create add score button
        addScoreButton = Button(fieldButtonFrame, text="Set Score")
        addScoreButton.pack(side=LEFT)
        addScoreButton.bind("<Button-1>", self.playerDone)


    def addRoundRow(self, roundText, rowLabelStyle = ()):
        """adds a new round row, 
        set rowLabelStyle to a tuple (framestyle, labelstyle) to overide round alterning"""
        if rowLabelStyle:
            rowStyle, labelStyle = rowLabelStyle
        else:
            rowStyle, labelStyle = self.currentRound % 2 and ("WHT.TFrame", "WHT.TLabel") or ("GRAY.TFrame", "GRAY.TLabel")
             
        rowFrame = Frame(self.roundFrame, style=rowStyle)
        rowFrame.pack(fill=BOTH)
        roundLabel = Label(rowFrame, text=roundText, font=self.customFont, style=labelStyle)
        roundLabel.pack()
        
    def addScoreRow(self, player, rowLabelStyle = ()):
        """adds a new score row for player, 
        set rowLabelStyle to a tuple (framestyle, labelstyle) to overide round alterning"""
        if rowLabelStyle:
            rowStyle, labelStyle = rowLabelStyle
        else:
            rowStyle, labelStyle = self.currentRound % 2 and ("WHT.TFrame", "WHT.TLabel") or ("GRAY.TFrame", "GRAY.TLabel") 
        rowFrame = Frame(self.playerFrameList[self.playerList.index(player)], style=rowStyle)
        rowFrame.pack(fill=BOTH)
        roundLabel = Label(rowFrame, text=str(player.score), font=self.customFont, style=labelStyle)
        roundLabel.pack()
        
    def initUI(self):
        if self.currentGameFrame:
            self.currentGameFrame.pack_forget()
            self.currentGameFrame.destroy()
        self.currentGameFrame = Frame(self.gameFrame)
        self.currentGameFrame.pack(fill=BOTH, expand=1)
        self.addSetScoreFrame(self.currentGameFrame)
        self.addRoundFrame(self.currentGameFrame)
        self.playerFrameList = []
        for player in self.playerList:
            # add border between players
            borderFrame = Frame(self.currentGameFrame, style="BLK.TFrame")
            borderFrame.pack(fill=BOTH, side=LEFT)    
            self.addPlayerFrame(self.currentGameFrame, player)
            
    def nextPlayer(self):
        "sets currentplayer to next player. if index = 0 its a new round"
        playerIndex = (self.playerList.index(self.currentPlayer) + 1) % len(self.playerList)
        self.currentPlayer = self.playerList[playerIndex]
        if playerIndex == 0:
            self.currentRound += 1
        return playerIndex
    
    def startNewGame(self):
        self.initUI()
        self.currentRound = 0
        self.currentPlayer = self.playerList[0]
        for player in self.playerList:
            player.score = self.startScore
    
    def victory(self, player):
        self.playerTotalScoreDict[player] += 1
    
    def __init__(self, gameFrame, playerList):
        '''
        Constructor
        '''
        self.setStyles()
        self.currentRound = 0
        self.playerList = playerList
        self.playerTotalScoreDict = dict.fromkeys(self.playerList, 0)
        self.currentPlayer = self.playerList[0]
        self.currentGameFrame = None
        self.gameFrame = gameFrame