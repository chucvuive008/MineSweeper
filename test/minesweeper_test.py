import unittest
import types
from minesweeper import *

class MineSweeperTest(unittest.TestCase):                       
  def setUp(self):
    self.minesweeper = MineSweeper()
      
  def Canary(self):
    self.assertTrue(True)
    
  def test_expose_cell(self):
    self.minesweeper.expose_cell(1,2)

    self.assertEqual(CellState.EXPOSED, self.minesweeper.cell_state(1,2))
    
  def test_expose_another_cell(self):
      self.minesweeper.expose_cell(2,3)

      self.assertEqual(CellState.EXPOSED, self.minesweeper.cell_state(2,3))
      
  def test_already_expose_cell(self):
      self.minesweeper.expose_cell(1,2)
      self.minesweeper.expose_cell(1,2)

      self.assertEqual(CellState.EXPOSED, self.minesweeper.cell_state(1,2))
    
   
  def test_out_of_row(self):
      try:
        self.minesweeper.expose_cell(11,3)
        fail("Expected exception for steping out of bound")
      except IndexError:
        assert True
        
  def test_out_if_column(self):
      try:
          self.minesweeper.expose_cell(3,11)
          fail("Expected exception for stepping out of bound")
      except IndexError:
          assert True  
            
   
  def test_expose_cell_calls_expose_neigbhor(self):
      def fake_expose_neighbor(self, row, column):
            self.row_given = row
            self.column_given = column
    
      self.minesweeper.expose_neighbor = types.MethodType(fake_expose_neighbor, self.minesweeper)
      
      self.minesweeper.expose_cell(1, 2)
      
      self.assertEqual(1, self.minesweeper.row_given)
      self.assertEqual(2, self.minesweeper.column_given)

  def test_expose_cell_on_exposed_cell_does_not_call_expose_neigbhor(self):
      def fake_expose_neighbor(self, row, column):
            self.called = True
  
      self.minesweeper.expose_neighbor = types.MethodType(fake_expose_neighbor, self.minesweeper)
  
      self.minesweeper.expose_cell(1, 2)
      self.minesweeper.called = False
      self.minesweeper.expose_cell(1, 2)
  
      self.assertFalse(self.minesweeper.called)
    
  def test_expose_neighbor_calls_expose_cell(self):
      self.minesweeper.rows_and_columns = []

      def fake_expose_cell(self, row, column):
            if(row in range(0,10) and column in range(0,10)):
                self.rows_and_columns.append(row)
                self.rows_and_columns.append(column)
            
      
      self.minesweeper.expose_cell = types.MethodType(fake_expose_cell, self.minesweeper)
      
      self.minesweeper.expose_neighbor(1, 2)
        
      self.assertEqual([0, 1, 0, 2, 0, 3, 1, 1, 1, 2, 1, 3, 2, 1, 2, 2, 2, 3] , self.minesweeper.rows_and_columns)
    
  def test_expose_neighbor_top_left_corner(self):
      self.minesweeper.rows_and_columns = []

      def fake_expose_cell(self, row, column):
            if(row in range(0,10) and column in range(0,10)):
                self.rows_and_columns.append(row)
                self.rows_and_columns.append(column)
            
      
      self.minesweeper.expose_cell = types.MethodType(fake_expose_cell, self.minesweeper)
      
      self.minesweeper.expose_neighbor(0, 0)
        
      self.assertEqual([0, 0, 0, 1, 1, 0, 1, 1], self.minesweeper.rows_and_columns)
  
  def test_expose_neighbor_calls_top_right_corner(self):
      self.minesweeper.rows_and_columns = []

      def fake_expose_cell(self, row, column):
            if(row in range(0,10) and column in range(0,10)):
                self.rows_and_columns.append(row)
                self.rows_and_columns.append(column)
            
      
      self.minesweeper.expose_cell = types.MethodType(fake_expose_cell, self.minesweeper)
      
      self.minesweeper.expose_neighbor(0, 9)

      self.assertEqual([0, 8, 0, 9, 1, 8, 1, 9], self.minesweeper.rows_and_columns)
    
  def test_expose_neighbor_calls_bottom_right_corner(self):
      self.minesweeper.rows_and_columns = []

      def fake_expose_cell(self, row, column):
            if(row in range(0,10) and column in range(0,10)):
                self.rows_and_columns.append(row)
                self.rows_and_columns.append(column)
            
      
      self.minesweeper.expose_cell = types.MethodType(fake_expose_cell, self.minesweeper)
      
      self.minesweeper.expose_neighbor(9, 9)

      self.assertEqual([8, 8, 8, 9, 9, 8, 9, 9], self.minesweeper.rows_and_columns)  
    
  def test_expose_neighbor_top_left_corner(self):
      self.minesweeper.rows_and_columns = []

      def fake_expose_cell(self, row, column):
            if(row in range(0,10) and column in range(0,10)):
                self.rows_and_columns.append(row)
                self.rows_and_columns.append(column)
            
      
      self.minesweeper.expose_cell = types.MethodType(fake_expose_cell, self.minesweeper)
      
      self.minesweeper.expose_neighbor(9, 0)
        
      self.assertEqual([8, 0, 8, 1, 9, 0, 9, 1], self.minesweeper.rows_and_columns)

  def test_seal_cell(self):
      self.minesweeper.toggle_cell(1, 2)

      self.assertEqual(CellState.SEAL, self.minesweeper.cell_state(1, 2))
    
  def test_unseal_cell(self):
      self.minesweeper.toggle_cell(1, 2)
      self.minesweeper.toggle_cell(1, 2)

      self.assertEqual(CellState.UNEXPOSED, self.minesweeper.cell_state(1, 2))
        
  def test_seal_cell_out_of_row(self):
      try: 
        self.minesweeper.toggle_cell(11, 4)
        fail("out of bound")
      except IndexError:
        assert True
     
  def test_seal_cell_out_of_column(self):
      try: 
        self.minesweeper.toggle_cell(5, 12)
        fail("out of bound")
      except IndexError:
        assert True
        
  def test_unseal_cell_out_of_row(self):
      try:
        self.minesweeper.toggle_cell(12, 5)
        self.minesweeper.toggle_cell(12, 5)
        fail("out of bound")
      except IndexError:
        assert True

  def test_unseal_cell_out_of_column(self):
      try:
        self.minesweeper.toggle_cell(2, 15)
        self.minesweeper.toggle_cell(2, 15)
        fail("out of bound")
      except IndexError:
        assert True
        
  def test_seal_cell_of_expose_cell(self):
      self.minesweeper.expose_cell(1, 2)
      self.minesweeper.toggle_cell(1, 2)

      self.assertEqual(CellState.EXPOSED, self.minesweeper.cell_state(1, 2))
        
  def test_expose_cell_of_seal_cell(self):
      self.minesweeper.toggle_cell(1, 2)
      self.minesweeper.expose_cell(1, 2)

      self.assertEqual(CellState.SEAL,self.minesweeper.cell_state(1, 2))
      self.assertEqual(CellState.UNEXPOSED, self.minesweeper.cell_state(0, 2))
    
  def test_check_game_state_no_expose_no_seal(self):

      self.assertEqual(GameState.INPROGRESS, self.minesweeper.check_game_state())

  def test_check_game_state_one_unexposed_cell(self):

      for i in range(10):
          self.minesweeper.toggle_cell(0,i)
      
      self.minesweeper.expose_cell(1, 5)
      self.minesweeper.cells[4][3] = CellState.UNEXPOSED

      self.assertEqual(GameState.INPROGRESS, self.minesweeper.check_game_state())
      

  def test_check_game_state_expose_mine(self):
      self.minesweeper.cellType[4][4] = 9
      self.minesweeper.expose_cell(4, 4)

      self.assertEqual(GameState.LOSE, self.minesweeper.check_game_state())

  def test_check_game_state_win(self):
      for i in range(10):
          self.minesweeper.cellType[0][i] = 9
          self.minesweeper.toggle_cell(0, i)

      for i in range(1, 10):
          for j in range(10):
              self.minesweeper.cells[i][j] = CellState.EXPOSED
      
      self.assertEqual(GameState.WIN, self.minesweeper.check_game_state())

  def test_for_create_10_mine(self):
      self.minesweeper.setGameBoard()
      countMine = 0
      for i in range(10):
          for j in range(10):
              if(self.minesweeper.cellType[i][j] == 9):
                    countMine = countMine + 1
        
      self.assertEqual(10, countMine)

  def test_for_random_generate_mine(self):
      self.anotherMinsweeper = MineSweeper()
      self.anotherMinsweeper.setGameBoard()
      self.minesweeper.setGameBoard()
      mineLoc = []
      mineLoc2 = []

      for i in range(10):
          for j in range(10):
              if(self.minesweeper.cellType[i][j] == 9):
                  mineLoc.append(i)
                  mineLoc.append(j)
              if(self.anotherMinsweeper.cellType[i][j] == 9):
                  mineLoc2.append(i)
                  mineLoc2.append(j)


      self.assertNotEqual(mineLoc, mineLoc2)

  def test_expose_cell_have_mine_neighbor(self):
       self.minesweeper.cellType[2][2] = 9
       self.minesweeper.expose_cell(2, 1)
  
       num_neighbor_not_expose = 0
  
       for i in range(1, 4):
           for j in range(0, 3):
               if(i != 2 or j != 1):
                   if(self.minesweeper.cells[i][j] == CellState.UNEXPOSED):
                       num_neighbor_not_expose = num_neighbor_not_expose + 1
  
       self.assertEqual(8, num_neighbor_not_expose)
       self.assertEqual(1, self.minesweeper.cellType[2][1])

if __name__ == '__main__':
    unittest.main()
