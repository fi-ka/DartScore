'''
Created on 28 mar 2013

@author: Expert
'''
from tkinter.constants import BOTH, TOP, LEFT
from tkinter.ttk import Style, Frame, Label

class Game301(object):
    '''
    Represents a game of 301
    '''
    
    def addPlayerInterface(self, gameFrame):
        "adds a player column to the interface"
        # styles
        style = Style()
        style.configure("GRN.TLabel", background="#ACF059")
        style.configure("GRN.TFrame", background="#ACF059")
        style.configure("GR.TFrame", background="#E0E0C8")
        style.configure("BLK.TFrame", background="black")
        
        # create player frame 
        playerFrame = Frame(gameFrame, style="GR.TFrame")
        playerFrame.pack(side=LEFT, fill=BOTH, expand = 1)
        
        # create top frame
        headerFrame = Frame(playerFrame, style="GRN.TFrame", padding=8)
        headerFrame.pack(fill=BOTH, side=TOP)
        nameLabel = Label(headerFrame, text="player", style="GRN.TLabel")
        nameLabel.pack(side=TOP)
        
        # create black border
        borderFrame = Frame(playerFrame, style="BLK.TFrame")
        borderFrame.pack(fill=BOTH, side=TOP)


    def __init__(self, gameFrame, playerList):
        '''
        Sets up the interface and variables for a game of 301
        '''
        self.playerList = playerList
        self.addPlayerInterface(gameFrame)
        self.addPlayerInterface(gameFrame)
        
        
        