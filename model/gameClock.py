'''
Created on 6 apr 2013

@author: Filip
'''
from model.game import Game

class GameClock(Game):
    '''
    Represents a game of Clock
    '''

    def playerDone(self, event):
        """Sets the score for the player and 
        handles what happens when a player is done with his turn"""
        # set score
        try:
            self.handleScore(self.currentPlayer, int(self.scoreVar.get()))
            self.addScoreRow(self.currentPlayer)
            
            newRound = not self.nextPlayer()
            if newRound:
                winner = self.goalCheck()
                if winner:
                    self.victory(winner)
                self.addRoundRow(self.currentRound)
        except ValueError:
            return
    
    def goalCheck(self):
        "Check if the game is won by any player"
        if self.currentRound == 21:
            maxScore = max([player.score for player in self.playerList])
            winner = self.playerList.index(maxScore) 
            return winner
        return None
    
    def handleScore(self, player, score):
        "Calculates the current total score for player, score is the score for last turn"    
        player.score += score
            
    def victory(self, player):
        "handles post-game, player won the game"
        Game.victory(self, player)
        self.startNewGame()
            
    def startNewGame(self):
        "starts a new game of X01. sets up rounds and initial score for players"
        Game.startNewGame(self)
        self.addRoundRow("", (self.styleWhiteFrame, self.styleWhiteLabel))
        for player in self.playerList:
            self.addScoreRow(player, (self.styleWhiteFrame, self.styleWhiteLabel))
        self.addRoundRow(self.currentRound)
    

    def __init__(self, gameFrame, playerList, startScore=0):
        '''
        Constructor
        '''
        Game.__init__(self, gameFrame, playerList)
        self.startScore = startScore
        self.startNewGame()