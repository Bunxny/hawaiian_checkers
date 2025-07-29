import copy

class Board:
    def __init__(self): #constructor
        self.theBoard = [] # will store a list of lists for an 8 by 8
        self.check = True # might be used to check validity
        self.color = None # used to indicate who turn it is
    
    def initializeBoard(self):
        for i in range(8):
            row = []
            for j in range(8):
                if (i + j) % 2 == 0: # if even
                    row.append("X")
                else:
                    row.append("O")
            self.theBoard.append(row)

    def printBoard(self):
        for row in self.theBoard:
            print(row, "\n")

    def moveSelection(self):
        selection = input("Which piece to which position? (Row,Column,Row,Column): ")
        return selection

    def opponentColor(self, color):
        # Change color output char
        if color == 'X':
            return 'O'
        elif color == 'O':
            return 'X'
        else:
            raise ValueError(f"Invalid color: {color}")
    
    def switchPlayer(self):
        # Change the object color to the opponent's color
        if self.color == 'X':
            self.color = 'O'
        else:
            self.color = 'X'

    def oneStep(self, selection):
        row1 = int(selection[0])
        col1 = int(selection[2])
        row2 = int(selection[4])
        col2 = int(selection[6])
        if (row2 == row1 + 2) or (row2 == row1 - 2) or (col2 == col1 + 2) or (col2 == col1 - 2):
            return True
        else:
            return False

    def ruleCheck(self, selection, color):
        try:
            row1 = int(selection[0]) 
            col1 = int(selection[2]) 
            row2 = int(selection[4]) 
            col2 = int(selection[6]) 

            piece = self.theBoard[row1][col1]
            spot = self.theBoard[row2][col2]

            if (piece != color):
                # print(selection)
                # print(piece)
                # print(self.color)
                # self.printBoard()
                # print("Invalid move: Not your piece.")
                return False

            if (spot != ' ' or not self.oneStep(selection)):
                # print("Invalid move: Can only move two spaces and into an empty spot.")
                return False

            if (row1 > row2 and col1 == col2):
                if (self.theBoard[row1 - 1][col1] == self.opponentColor(color)):
                    self.theBoard[row1 - 1][col1] = ' '
                else:
                    #print("Invalid move: Must capture an opponent's piece.")
                    return False
            elif (row1 < row2 and col1 == col2):
                if (self.theBoard[row1 + 1][col1] == self.opponentColor(color)):
                    self.theBoard[row1 + 1][col1] = ' '
                else:
                    # print("Invalid move: Must capture an opponent's piece.")
                    return False
            elif (col2 < col1 and row1 == row2):
                if (self.theBoard[row1][col1 - 1] == self.opponentColor(color)):
                    self.theBoard[row1][col1 - 1] = ' '
                else:
                    # print("Invalid move: Must capture an opponent's piece.")
                    return False
            elif (col2 > col1 and row1 == row2):
                if (self.theBoard[row1][col1 + 1] == self.opponentColor(color)):
                    self.theBoard[row1][col1 + 1] = ' '
                else:
                    # print("Invalid move: Must capture an opponent's piece.")
                    return False
            else:
                # print("Invalid move: Can only move LRUD and need to be capturing.")
                return False
        except:
            print("unexpected error")
            return False

        self.theBoard[row1][col1] = ' '
        self.theBoard[row2][col2] = color
        # print(True)
        return True

    def multiJump(self, selection):
        board_copy = copy.deepcopy(self)
        row1 = int(selection[0])
        col1 = int(selection[2])
        row2 = int(selection[4])
        col2 = int(selection[6])
        progress = True  # Initialize to True for the first jump

        while progress:
            # print("su")
            if (row1 > row2 and col1 == col2):
                row1 = row2
                row2 = row2 - 2
                # print("sup")
            elif (row1 < row2 and col1 == col2):
                row1 = row2
                row2 = row2 + 2
                # print("sdown")
            elif (col2 < col1 and row1 == row2):
                col1 = col2
                col2 = col2 - 2
                # print("sleft")
            elif (col2 > col1 and row1 == row2):
                col1 = col2
                col2 = col2 + 2
                # print("sright")
            else:
                print("Unexpected error")

            newSelection = str(row1) + "," + str(col1) + "," + str(row2) + "," + str(col2)
            if board_copy.ruleCheck(newSelection, self.color):
                answer = input("Continue jump? (y or n): ")
                print(newSelection)
                if answer == 'y':
                    self.ruleCheck(newSelection, self.color)
                    # print(self.theBoard)
                    # Continue the jump
                else:
                    progress = False
            else:
                print("Max move")
                progress = False  # No valid progress
    
    def multi(self, selection):
        board_copy = copy.deepcopy(self)
        row1 = int(selection[0])
        col1 = int(selection[2])
        row2 = int(selection[4])
        col2 = int(selection[6])
        progress = True  # Initialize to True for the first jump

        while progress:
            # print("su")
            if (row1 > row2 and col1 == col2):
                row1 = row2
                row2 = row2 - 2
                # print("sup")
            elif (row1 < row2 and col1 == col2):
                row1 = row2
                row2 = row2 + 2
                # print("sdown")
            elif (col2 < col1 and row1 == row2):
                col1 = col2
                col2 = col2 - 2
                # print("sleft")
            elif (col2 > col1 and row1 == row2):
                col1 = col2
                col2 = col2 + 2
                # print("sright")
            else:
                print("Unexpected error")

            newSelection = str(row1) + "," + str(col1) + "," + str(row2) + "," + str(col2)
            if board_copy.ruleCheck(newSelection, self.color):
                answer =  'y'
                print("new:" + newSelection)
                if answer == 'y':
                    self.ruleCheck(newSelection, self.color)
                    # print(self.theBoard)
                    # Continue the jump
                else:
                    progress = False
            else:
                print("Max move")
                progress = False  # No valid progress

    def generateValidMoves(self, color):
        # dictionary to store valid moves for each piece
        valid_moves = {}
        # Right, Left, Down, and Up
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        # Iterating through each spot in the board
        for row1 in range(8):
            for col1 in range(8):
                board_copy = copy.deepcopy(self)
                # Check if the spot is current player's color
                if board_copy.theBoard[row1][col1] == color:
                    # empty list
                    #valid_moves[f"{row1},{col1}"] = []

                    # Iterating through each direction up, down, left, right
                    for dr, dc in directions:
                        # destination cell
                        row2, col2 = row1 + dr, col1 + dc
                        # Check if destination is within the board boundaries
                        if 0 <= row2 < 8 and 0 <= col2 < 8:
                            # format "row1,col1,row2,col2"
                            move = f"{row1},{col1},{row2},{col2}"
                            # print(move)
                            # Check if the move is valid 
                            if board_copy.ruleCheck(move, color):
                                # Add the valid move to the list
                                valid_moves[f"{row1},{col1}"] = []
                                valid_moves[f"{row1},{col1}"].append(f"{row2},{col2}")
                            board_copy = copy.deepcopy(self)

        # for position, moves in valid_moves.items():
        #     if moves:
        #         print(f"can move {position},{', '.join(moves)}")

        # Return the dictionary of valid moves
        # print("from" + str(valid_moves))
        return valid_moves

    
    def winCheck(self):
        board_copy = copy.deepcopy(self)
        valid_moves = board_copy.generateValidMoves('X')
        
        opponent_board_copy = copy.deepcopy(self)
        valid_moves_opponent = opponent_board_copy.generateValidMoves('O')
        
        # print("Valid Moves for current player:", self.color,  valid_moves)
        # print("Valid Moves for opponent player:", opponent_color,  valid_moves_opponent)
        
        if not valid_moves and not valid_moves_opponent:
            return 0  # Draw
        elif not valid_moves:
            return 1  # White wins
        elif not valid_moves_opponent:
            return 2  # Black wins
        return 3


    def firstTwoMoves(self):
        print("Black (3,3) and White (3,4) are removed at the start")
        self.theBoard[3][3] = ' '
        self.theBoard[3][4] = ' '

    def evaluate(self):
        # pieces for the current player and oponent
        piece_count = sum(row.count(self.color) for row in self.theBoard)
        opiece_count = sum(row.count(self.opponentColor(self.color)) for row in self.theBoard)
        # number of moves for the current player and the opponent
        player_moves_count = len(self.generateValidMoves(self.color))
        opponent_color = self.opponentColor(self.color)
        opponent_moves_count = len(self.generateValidMoves(opponent_color))

        # Calculate the difference
        moves_difference = player_moves_count - opponent_moves_count
        piece = piece_count - opiece_count
        # Adjust the weight as needed
        weight_pieces = .3  
        weight_moves = 2 

        # Calculate the evaluation using the weighted components
        evaluation = weight_pieces * piece_count + weight_moves * moves_difference
        
        return evaluation

    def minimax(self, depth, alpha, beta, maximizing_player, player_color, opponent_color):
        if depth == 0:
            return self.evaluate()

        valid_moves = self.generateValidMoves(player_color) if maximizing_player else self.generateValidMoves(opponent_color)

        if maximizing_player:
            max_eval = -float("inf")
            for start_position, end_positions in valid_moves.items():
                for move in end_positions:
                    board_copy = copy.deepcopy(self)
                    board_copy.ruleCheck(f"{start_position},{move}", player_color)
                    eval = board_copy.minimax(depth - 1, alpha, beta, False, player_color, opponent_color)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float("inf")
            for start_position, end_positions in valid_moves.items():
                for move in end_positions:
                    board_copy = copy.deepcopy(self)
                    board_copy.ruleCheck(f"{start_position},{move}", opponent_color)
                    eval = board_copy.minimax(depth - 1, alpha, beta, True, player_color, opponent_color)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval

    def findBestMove(self, depth):
        best_move = None
        best_eval = -float("inf")
        alpha = -float("inf")
        beta = float("inf")
        
        if self.color == 'X':
            player_color = 'X'
            opponent_color = 'O'
        else:
            player_color = 'O'
            opponent_color = 'X'
        
        valid_moves = self.generateValidMoves(player_color)
        
        for start_position, end_positions in valid_moves.items():
            for move in end_positions:
                board_copy = copy.deepcopy(self)
                board_copy.ruleCheck(f"{start_position},{move}", player_color)
                eval = board_copy.minimax(depth - 1, alpha, beta, False, player_color, opponent_color)
                alpha = max(alpha, eval)
                if eval > best_eval:
                    best_eval = eval
                    best_move = f"{start_position},{move}"
                if beta <= alpha:
                    break
        return best_move


def main():
    color_choice = input("Choose your color (X or O): ")
    
    if color_choice not in ['X', 'O']:
        print("Invalid color choice. Please choose 'X' or 'O'.")
        return
    
    board_object = Board()
    board_object.initializeBoard()
    board_object.color = color_choice
    board_object.firstTwoMoves()
    
    while True:
        print("Player: " + board_object.color)
        board_object.printBoard()
        win = board_object.winCheck()
        if win == 0:
            print("Draw")
            break
        elif win == 1:
            print("White wins")
            break
        elif win == 2:
            print("Black wins")
            break
        player = board_object.color
        oplayer = board_object.opponentColor(board_object.color)
        valid_moves = board_object.generateValidMoves(board_object.color)
        validMoves = board_object.generateValidMoves(board_object.opponentColor(board_object.color))
        print(f"Opponent player can move: {oplayer}")
        for position, moves in validMoves.items():
            if moves:
                moves_str = ', '.join(moves)
                print(f"{position},{moves_str}")
        print(f"Current player can move: {player}")
        for position, moves in valid_moves.items():
            if moves:
                moves_str = ', '.join(moves)
                print(f"{position},{moves_str}")
                
        if board_object.color == color_choice:
            move = board_object.moveSelection()
            while not board_object.ruleCheck(move, board_object.color):
                print("Invalid move. Try again.")
                move = board_object.moveSelection()
            board_object.multiJump(move)
        else:
            # AI's turn
            depth = 3
            if not board_object.generateValidMoves(board_object.color):
                print("No valid moves for AI. It passes.")
            else:
                best_move = board_object.findBestMove(depth)
                board_object.ruleCheck(best_move, board_object.color)
                board_object.multiJump(best_move)
                print(f"AI's move: {best_move}")

        board_object.switchPlayer()

if __name__ == "__main__":
    main()
