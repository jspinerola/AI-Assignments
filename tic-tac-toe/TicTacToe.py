"""
Tic-Tac-Toe with Tkinter
File: TicTacToe.py
Author: Julian Spindola, Texas A&M University-San Antonio
Date Modified: 06-06-2025
"""

# Import necessary libraries
import tkinter as tk
from tkinter import PhotoImage

# Class that defines a cell. Extends Tkinter's `Label` class.
class Cell(tk.Label):
  
  def __init__(self, root):
    super().__init__(root)  
    self.image = PhotoImage(file="empty.gif")
    self.token = ""

    self.bind('<Button-1>', set_image)

    self.config(image=self.image) 

# Called at each click. Sets image, handles turn logic, and win and tie conditions 
def set_image(event):
  # Initialize global variables "turn", "cell", and "turn_count"
  global turn
  global cells
  global turn_count
  
  # Assign current cell value to cell variable
  cell = event.widget

  # Ensures that cell can only be activated when cell is empty
  if cell.token != "":
    return
  
  # Increment turn count
  turn_count += 1

  # If the current turn is O...
  if turn == "O":
    # Set the image to an "O"
    cell.config(image=pic_o)
    # Set the cell's token to "O"
    cell.token = "O"
    # Check if the win condition has been met
    isWon(cell, cell.master)
    # If not, check if there is a tie
    isFull(cell.master)
    # Else, switch turn to X
    turn = "X"
  else:
    # Set the image to an "X"
    cell.config(image=pic_x)
    # Set the cell's token to "X"
    cell.token = "X"
    # Check if the win condition has been met
    isWon(cell, cell.master)
    # If not, check if there is a tie
    isFull(cell.master)
    # Else, switch turn to O
    turn = "O"

# Checks if the current user's turn has won 
def isWon(cell, root):
  # Displays token that won and "Restart Game" button 
  def displayWinInfo(token):        
    msg = token + " won the game! Play again?"

    win_frame = tk.Frame(root)
    win_frame.grid(row=3, column=0, columnspan=3)

    label = tk.Label(win_frame, text=msg)
    restart_button = tk.Button(win_frame, text="Restart", command=lambda: restart_window(root))

    label.pack()
    restart_button.pack()

  # Initialize global cells variable
  global cells
  token = cell.token

  # Get current cell's row and column 
  info = cell.grid_info()
  row = info["row"]
  col = info["column"]

  # Check row
  for i in range(3):
    key = (row, i)
    if cells[key].token != token:
      break
  else:
    displayWinInfo(token)
    return
  
  # Check col
  for i in range(3):
    key = (i, col)
    if cells[key].token != token:
      break
  else:
    displayWinInfo(token)
    return
  
  # Check Diagonal
  if col == row:
    for i in range(3):
      key = (i, i)
      if cells[key].token != token:
        break
    else:
      displayWinInfo(token)
      return
    
  # Check Antidiagnoal
  if col + row == 2:
    for i in range(3):
      key = (i, 2 - i)
      if cells[key].token != token:
        break
    else: 
      displayWinInfo(token)
      return
   # If no win...
    return None

# Checks if the current game board is full. Tie condition
def isFull(root):
  # Initialize global variable turn_count
  global turn_count

  # If board is full
  if turn_count == 9:
    # Display message and restart button 
    msg = "There was a tie! Play again?"

    win_frame = tk.Frame(root)
    win_frame.grid(row=3, column=0, columnspan=3)

    label = tk.Label(win_frame, text=msg)
    restart_button = tk.Button(win_frame, text="Restart", command=lambda: restart_window(root))

    label.pack()
    restart_button.pack()

# Function that restarts the game window
def restart_window(root):
  global pic_empty, pic_x, pic_o
  root.destroy()
  new_window = tk.Tk()
  
  # Reload images
  pic_empty = PhotoImage(file="empty.gif")
  pic_x = PhotoImage(file="x.gif")
  pic_o = PhotoImage(file="o.gif")
  
  buildGame(new_window)

  new_window.mainloop()

# Function that initializes game window and builds cells
def buildGame(root):
  root.title("Tic-tac-toe")
  root.geometry("200x250")

  # Global Variables
  global cells
  global turn
  global turn_count
  cells = {}
  turn = "O"
  turn_count = 0

  # Build Grid of Cells
  for i in range(3):
    for j in range(3):
      cell = Cell(root)
      cell.grid(row = i, column = j)
      cells[(i, j)] = cell

window = tk.Tk()

pic_empty = PhotoImage(file="empty.gif")
pic_x = PhotoImage(file="x.gif")
pic_o = PhotoImage(file="o.gif")

buildGame(window)

window.mainloop()