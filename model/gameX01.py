'''
Created on 28 mar 2013

@author: Expert
'''
from model.game import Game


class GameX01(Game):
    '''
    Represents a game of 301
    '''   
    
    def playerDone(self, event):
        """Sets the score for the player and 
        handles what happens when a player is done with his turn"""
        # set score
        try:
            self.handleScore(self.currentPlayer, int(self.scoreVar.get()))
            self.addScoreRow(self.currentPlayer)
            
            winner = self.goalCheck()
            if winner:
                self.victory(winner)
            else:
                newRound = not self.nextPlayer()
                if newRound:
                    self.addRoundRow(self.currentRound)
        except ValueError:
            return
    
    def goalCheck(self):
        "Check if the game is won by any player"
        for player in self.playerList:
            if player.score == 0:
                return player
        return None
    
    def handleScore(self, player, score):
        "Calculates the current total score for player, score is the score for last turn"
        if player.score - score == 0:
            player.score -= score
        elif player.score - score > 0:    
            player.score -= score
            
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
        
        
        
    def __init__(self, gameFrame, playerList, startScore=301):
        '''
        Sets up the interface and variables for a game of 301
        '''
        Game.__init__(self, gameFrame, playerList)
        self.startScore = startScore
        self.startNewGame()
        
        
