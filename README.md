### Report
The first thing that this program does is ask the player which color they want to be.
```
python3 Board.py
Choose your color (X or O):
```
After that, the program sets up the board, as instructed. It does that by adding in ‘X’s and ‘O’s in alternating order to create an 8x8 grid filled with Xs and Os. The next step is the removal of the first pieces, (4,4) and (4,5) and informing the player as such (the numbering of the 8x8 board is 0-7 and empty spots are indicated by  ‘  ‘ as these are just preferences we prefer that can be easily changed). Next, a list of all the possible moves for both the AI and the player at this specific board state are printed. These moves are generated from a function/method “generateValidMoves”, which checks to see if a move for a specific color is valid by sending any possible combination of moves, which it determines by seeing if there is a spot two above, two below, two to the right or two to the left of said piece that is within the board. That combination is sent to the “ruleCheck” function which sees if it has a piece of the opposite color right next to it and if there is an empty space right next to the opponent’s piece in the same direction. If the possible move is acceptable, then it gets sent right back to the “generateValidMoves”, where it is put in a dictionary and then returned once all moves are calculated for a specific piece.

```
Black (3,3) and White (3,4) are removed at the start
Player: X
['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'] 

['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', ' ', ' ', 'X', 'O', 'X'] 

['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'] 

['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'] 

Opponent player can move: O
1,4,3,4
3,6,3,4
5,4,3,4
Current player can move: X
1,3,3,3
3,1,3,3
5,3,3,3
Which piece to which position? (Row,Column,Row,Column): 
```

After all the moves are calculated and then printed, the next step depends on who is going: the AI or the human player. If the player is going, they just input one of the possible moves and the board updates based on the move. If the AI is going, then it gets fun.

```
Which piece to which position? (Row,Column,Row,Column): 1,3,3,3
Max move
Player: O
['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', ' ', 'O', 'X', 'O', 'X'] 

['X', 'O', 'X', ' ', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', 'X', ' ', 'X', 'O', 'X'] 

['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'] 

['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'] 

Opponent player can move: X
1,1,1,3
1,5,1,3
Current player can move: O
1,4,3,4
2,1,2,3
2,5,2,3
3,2,3,4
3,6,3,4
4,3,2,3
5,4,3,4
```

The AI algorithm uses the standard minimax algorithm. The algorithm takes in a board object, the depth so far, alpha and beta values for pruning as parameters. It also takes a boolean ‘maximizing player’ as a parameter based on which valid moves are generated. For each move, it creates a deep copy of the state, applies the move and recursively calls the function with the new state. “findBestMove” function also creates a deep copy of the board, applies the move, and generates the evaluation using the “minimax” function. Creating a deep copy of the board is computationally expensive which may be causing a “too many copies” issue. The AI evaluates not just the current state of the board but the future state of the board as well. In order to do that, minimax with alpha-beta pruning is required. This exact process depends on whether or not minimax is at a ‘min’ stage or a ‘max’ stage. Alpha-beta pruning is applied in the “findBestMove” function where if ‘beta’ is less than or equal to ‘alpha’, the loop is “pruned” or broken.

The static evaluation function calculates the heuristics of how many pieces are on the board and how many moves each player can make. This information is then all put into a score with moves being weighted higher than pieces. This will be used in the minimax function helping the algorithm decide which is the best move. The best move should be the one that gives the AI more moves than the player as the winner of the game must still be able to make moves in the end.

```
Max move
AI's move: 4,3,2,3
Player: X
['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', ' ', 'O', 'X', 'O', 'X'] 

['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', ' ', ' ', 'X', 'O', 'X'] 

['X', 'O', 'X', ' ', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'] 

['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'] 

['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
```

