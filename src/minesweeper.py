from random import *
from enum import Enum

class CellState(Enum):
    UNEXPOSED   = "UNEXPOSED"
    EXPOSED     = "EXPOSED"
    SEAL        = "SEAL"
  
class GameState(Enum):
    INPROGRESS  = "INPROGRESS"
    LOSE        = "LOSE"
    WIN         = "WIN"

class MineSweeper:
  def __init__(self):
    self.cells = [[CellState.UNEXPOSED for i in range(10)] for j in range(10)]
    self.cellType = [[0 for i in range(10)] for j in range(10)]
    self.gameState = GameState.INPROGRESS
        
  def cell_state(self,row,column):
        return self.cells[row][column]


  def expose_cell(self, row, column):
    if(self.cells[row][column] == CellState.UNEXPOSED):
      self.cells[row][column] = CellState.EXPOSED
      self.check_neighbor(row, column)
         
      if(self.cellType[row][column] == 0):
        self.expose_neighbor(row, column)

  def expose_neighbor(self, row, column):
      
        for i in range(row-1,row+2):
          for j in range(column-1, column+2):
              if(i in range (10) and j in range(10)):
                  self.expose_cell(i,j)
      
                    

    
  def toggle_cell(self, row, column):              
      if(self.cells[row][column] == CellState.UNEXPOSED):
          self.cells[row][column] = CellState.SEAL
      elif(self.cells[row][column] == CellState.SEAL):
          self.cells[row][column] = CellState.UNEXPOSED
             
  def setGameBoard(self):
      mine_loc = sample(range(0, 100), 10)
      for i in mine_loc:
        row = i // 10
        column = i % 10
        self.cellType[row][column] = 9

  def check_neighbor(self, row, column):
      for i in range(row -1 , row + 2):
          for j in range(column -1, column + 2):
              if(i in range(10) and j in range(10)):

                if(i != row or j != column):
                    if(self.cellType[i][j] == 9):
                        self.cellType[row][column] = self.cellType[row][column] + 1

  def check_game_state(self):
      num_of_mine = 10
      num_of_non_mine = 90

      for i in range(10):
          for j in range(10):
              if(self.cellType[i][j] == 9 and self.cells[i][j] == CellState.EXPOSED ):
                  i = 9
                  j = 9
                  self.gameState = GameState.LOSE
              elif(self.cellType[i][j] == 9 and self.cells[i][j] == CellState.SEAL):
                  num_of_mine = num_of_mine - 1
              elif(self.cellType[i][j] != 9 and self.cells[i][j] == CellState.EXPOSED):
                  num_of_non_mine = num_of_non_mine -1
              
      if(num_of_mine == 0 and num_of_non_mine == 0):
          self.gameState = GameState.WIN
      return self.gameState


                         

      