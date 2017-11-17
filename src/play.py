from minesweeper import *
from tkinter import *

mine= MineSweeper()
mine.setGameBoard()


def make_board_game():
      print("   ", end="")
      for i in range(10):
          print(str(i) + " ", end = "")
        
      print("")
      print("-----------------------------------------------")
      for i in range (10):
            print(str(i) + " |" , end = "")
            for j in range (10):
                if(mine.cells[i][j] == CellState.UNEXPOSED):
                    print("C ", end="")
            print(" ")
      check = True
      while(mine.gameState == GameState.INPROGRESS):
        try:
            
            print("Please choose row, column for a cell you pick, then choose action you wanddddddadasdasdasdsat.")
            print("row number: ")
            row = int(input())
            print("column number: ")
            column = int(input())
            print("action (S for seal and E for expose")
            action = input()
            try: 
                if(action.lower() == "s"):
                    mine.toggle_cell(row, column)
                elif(action.lower() == "e"):
                    mine.expose_cell(row, column)
                else:
                    print("provide incorrect action. please make sure you type s or e")
            except IndexError:
                print("provide row or column out of range")
        except ValueError:
            print("provide invalid value. Please try again")
        
        print("   ", end="")
        for i in range(10):
          print(str(i) + " ", end = "")
        print("")
        print("-----------------------------------------------")
        for i in range (10):
            print(str(i) + " |" , end = "")
            for j in range (10):
                if(mine.cells[i][j] == CellState.UNEXPOSED):
                    print("C ", end ="")
                elif(mine.cells[i][j] == CellState.SEAL):
                    print("S ", end = "")
                else:
                    print(str(mine.cellType[i][j] )+ " ", end = "")
            print(" ")

        mine.check_game_state()
        if(mine.gameState == GameState.LOSE):
            print("you are Lose")
        elif(mine.gameState == GameState.WIN):
            print("You are Win")

make_board_game()