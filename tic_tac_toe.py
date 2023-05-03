import copy

X = "X"
O = "O"

def generate_moves(board):
  """Generates a list of all the valid moves that can be made from the given board state."""
  moves = []
  for i, row in enumerate(board):
    for j, cell in enumerate(row):
      if cell is None:
        moves.append((i, j))
  return moves

def terminal_test(board):
  """Determines whether the given board state is a terminal state (win or draw). Returns the winner if the game is won, "T" if the game is a draw, and None otherwise."""
  # Check for a win on the rows
  for row in board:
    if row[0] == row[1] == row[2]:
      return row[0]
  # Check for a win on the columns
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col]:
      return board[0][col]
  # Check for a win on the diagonals
  if board[0][0] == board[1][1] == board[2][2]:
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0]:
    return board[0][2]
  # Check for a draw
  for row in board:
    for cell in row:
      if cell is None:
        return None
  return "T"

def minimax(board, player, depth=0):
  """Implements the minimax algorithm to determine the best move for the given player on the given board. Returns a tuple of the form (score, move)."""
  # Check for terminal states
  result = terminal_test(board)
  if result is not None:
    if result == player:
      return (10 - depth, None)
    elif result == "T":
      return (0, None)
    else:
      return (-10 + depth, None)
  # Generate a list of all the possible next moves
  moves = generate_moves(board)
  # Initialize the best score and best move to negative infinity and None, respectively
  best_score = float("-inf")
  best_move = None
  # Iterate through the list of moves and determine the best one using minimax
  for move in moves:
    # Make a copy of the board and apply the move
    new_board = copy.deepcopy(board)
    new_board[move[0]][move[1]] = player
    # Recursively call minimax with the new board state and the opposite player
    if player == X:
      opponent = O
    else:
      opponent = X
    score, _ = minimax(new_board, opponent, depth + 1)
    # If the score is better than the current best score, update the best score and best move
    if score > best_score:
      best_score = score
      best_move = move
  return (best_score, best_move)

def play(board, player):
  """Plays a single move on the given board as the given player. Returns the new board state."""
  # Use the minimax function to determine the best move
  _, move = minimax(board, player)
  # Make a copy of the board and apply the move
  new_board = copy.deepcopy(board)
  new_board[move[0]][move[1]] = player
  return new_board

def play_game():
  """Plays a game of tic tac toe between a minimax agent and a human player."""
  board = [[None, None, None], [None, None, None], [None, None, None]]
  player = X
  while True:
    # Print the current board state
    print_board(board)
    # If it's the human player's turn, prompt them for their move
    if player == X:
      row = int(input("Enter the row for your move (0, 1, or 2): "))
      col = int(input("Enter the column for your move (0, 1, or 2): "))
      board[row][col] = X
    # If it's the agent's turn, use the minimax function to determine the best move
    else:
      _, move = minimax(board, player)
      board[move[0]][move[1]] = O
    # Check for a terminal state
    result = terminal_test(board)
    if result is not None:
      print_board(board)
      if result == X:
        print("X wins!")
      elif result == O:
        print("O wins!")
      else:
        print("It's a draw!")
      break
    # Switch players
    if player == X:
      player = O
    else:
      player = X


def print_board(board):
  """Prints the current board state to the console."""
  for row in board:
    print(row)

play_game()
