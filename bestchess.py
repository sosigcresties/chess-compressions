import random
from Chessnut import Game

pieces = {"p": "♙", "r": "♖", "n": "♘", "b": "♗", "q": "♕", "k": "♔", "P": "♟", "R": "♜", "N": "♞", "B": "♝", "Q": "♛", "K": "♚"}

chessgame = Game()

def print_game(chessgame):
  board = str(chessgame).split(" ")[0]
  print("  -------------------------")

  row_ct = 8
  for row in board.split('/'):
    print(row_ct, end=" ")
    row_ct -= 1
    for piece in row:
      if piece in pieces:
        print("|" + pieces[piece], end=" ")
      else:
        for i in range(int(piece)):
          print("| ", end=" ")
    print("|")
    print("  -------------------------")
  print("   A  B  C  D  E  F  G  H ")

turn = 0
end = 0

choice = input("Would you like to play against our \n highly specialised 10000 ELO rated AI (type A or a) \n or against a friend? (type B or b): ")
if choice in ["B", "b"]:
  print_game(chessgame)
  while not end:
    if turn%2 == 0:
      if len(chessgame.get_moves()) == 0:
        print("Checkmate! ")
        break
      move = input("White to play: ")
      while not move in chessgame.get_moves():
        print("Illegal move ")
        move = input("White to play: ") 
        
      if move in chessgame.get_moves():
        print("Move applied. ")
        chessgame.apply_move(move)
        
    elif turn%2 == 1:
      if len(chessgame.get_moves()) == 0:
        print("Checkmate! ")
        break
      move = input("Black to play: ")
      
      while not move in chessgame.get_moves():
        print("Illegal move ")
        move = input("Black to play: ")
        
      if move in chessgame.get_moves():
        print("Move applied. ")
        chessgame.apply_move(move)
    else:
      print("How did you get here, this was not meant to happen! ")
    print_game(chessgame)
    turn += 1

elif choice in ["A", "a"]: 
  sideChoice = input("Pick a side to play on. White (W/w) or Black (B/b): ")
  if sideChoice in ["W", "w"]:
    print_game(chessgame)
    while not end:
  
      if turn%2 == 1:
        if len(chessgame.get_moves()) == 0:
          print("Checkmate! ")
          break
        move = random.choice(chessgame.get_moves())
          
        if move in chessgame.get_moves():
          print("Stonkfish chose: " + move + " ")
          chessgame.apply_move(move)
  
      if turn%2 == 0:
        if len(chessgame.get_moves()) == 0:
          print("Checkmate! ")
          break
        move = input("White to play: ")
        while not move in chessgame.get_moves():
          print("Illegal move ")
          move = input("White to play: ") 
          
        if move in chessgame.get_moves():
          print("Move applied. ")
          chessgame.apply_move(move)
      
      else:
        print("How did you get here, this was not meant to happen! ")
      print_game(chessgame)
      turn += 1
  if sideChoice in ["B", "b"]:
    print_game(chessgame)
    while not end:
      if turn%2 == 0:
        if len(chessgame.get_moves()) == 0:
          print("Checkmate! ")
          break
        move = random.choice(chessgame.get_moves())
          
        if move in chessgame.get_moves():
          print("Stonkfish chose: " + move + " ")
          chessgame.apply_move(move)
            
      elif turn%2 == 1:
        if len(chessgame.get_moves()) == 0:
          print("Checkmate! ")
          break
        move = input("Black to play: ")
        
        while not move in chessgame.get_moves():
          print("Illegal move ")
          move = input("Black to play: ")
          
        if move in chessgame.get_moves():
          print("Move applied. ")
          chessgame.apply_move(move)
      else:
        print("How did you get here, this was not meant to happen! ")
      print_game(chessgame)
      turn += 1

import random
from Chessnut import Game

pieces = {"p": "♙", "r": "♖", "n": "♘", "b": "♗", "q": "♕", "k": "♔", "P": "♟", "R": "♜", "N": "♞", "B": "♝", "Q": "♛", "K": "♚"}

def count_points(chessgame):
  board = str(chessgame).split(" ")[0]
  print(board)
  white_points = 0 + board.count('P') * 1 + board.count('R') * 5 + board.count('N') * 3 + board.count('B') * 3.5 + board.count('Q') * 9 
  black_points = 0 + board.count('p') * 1 + board.count('r') * 5 + board.count('n') * 3 + board.count('b') * 3.5 + board.count('q') * 9 
  if black_points > white_points:
    return("black")
  elif white_points > black_points:
    return("white")
  else:
    return("draw")

  #rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR
  
def print_game(chessgame):
  board = str(chessgame).split(" ")[0]
  print("  -------------------------")

  row_ct = 8
  for row in board.split('/'):
    print(row_ct, end=" ")
    row_ct -= 1
    for piece in row:
      if piece in pieces:
        print("|" + pieces[piece], end=" ")
      else:
        for i in range(int(piece)):
          print("| ", end=" ")
    print("|")
    print("  -------------------------")
  print("   A  B  C  D  E  F  G  H ")
  
turn = 0

bots = []

games = 100

for i in range(0, games):
  chessgame = Game()
  end = 0
  turn = 0
  while not end:
    if turn%2 == 0:
      if len(chessgame.get_moves()) == 0:
        print("Checkmate! Black wins")
        bots.append("black")
        end = 1
        break
      move = random.choice(chessgame.get_moves())
      #print(f"{turn}. White moved " + move)
      chessgame.apply_move(move)
        
    elif turn%2 == 1:
      if len(chessgame.get_moves()) == 0:
        print("Checkmate! White wins")
        bots.append("white")
        end = 1
        break
      move = random.choice(chessgame.get_moves())
      #print(f"{turn}. Black moved " + move)
      chessgame.apply_move(move)
    else:
      print("How did you get here, this was not meant to happen! ")
    #print_game(chessgame)