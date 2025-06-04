import tkinter as tk
from tkinter import PhotoImage

# Initialize window
window = tk.Tk()
window.title("Tic-tac-toe")
window.geometry("400x400")
pic_empty = PhotoImage(file="empty.gif")
pic_x = PhotoImage(file="x.gif")
pic_o = PhotoImage(file="o.gif")
# Global Variable
turn = "O"

def set_image(event):
  # Initialize variables "turn" and "cell"
  global turn
  global cells
  # print(cells[(0, 0)].token)

  cell = event.widget

  # Ensures that cell can only be activated when cell is empty
  if cell.token != "":
    return

  if turn == "O":
    cell.config(image=pic_o)
    cell.token = "O"
    isWon(cell)
    turn = "X"
    # print(cell.token)
  else:
    cell.config(image=pic_x)
    cell.token = "X"
    turn = "O"
    # print(cell.token)

# Cell class
class Cell(tk.Label):
  def __init__(self):
    super().__init__(window)  
    self.image = PhotoImage(file="empty.gif")
    self.token = ""

    self.bind('<Button-1>', set_image)

    self.config(image=self.image) 

def isWon(cell):
  global cells
  token = cell.token

  info = cell.grid_info()
  row = info["row"]
  col = info["column"]

  # Check row
  for i in range(3):
    key = (row, i)
    if cells[key].token != token:
      break
  else:
    print(token + " Won!!!")
    return
  


cells = {}

# Build Grid of Cells
for i in range(3):
  for j in range(3):
    cell = Cell()
    cell.grid(row = i, column = j)
    cells[(i, j)] = cell




window.mainloop()