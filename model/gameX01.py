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
        for player in self.playerList:
            if player.score == 0:
                return player
        return None
    
    def handleScore(self, player, score):
        if player.score - score == 0:
            player.score -= score
        elif player.score - score > 0:    
            player.score -= score
            
    def victory(self, player):
        Game.victory(self, player)
        self.startNewGame()
            
    def startNewGame(self):
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
        
        
