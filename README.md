# CS50 Project 0: Tic-Tac-Toe

This project implements a simple **Tic-Tac-Toe** game using the **Minimax algorithm with alpha-beta pruning** to make optimal moves for the current player.

**Note**: I only created the `tictactoe.py` file; the `runner.py` file was provided by the course.

## About the Minimax Algorithm

The Minimax algorithm explores all possible moves in the game tree to choose the optimal move for the current player. It evaluates the game tree to maximize the current player's score while minimizing the opponent's score. The algorithm considers terminal states such as a win, loss, or draw and uses **alpha-beta pruning** to enhance performance by eliminating unnecessary calculations.

## Key Features

- **Alpha-Beta Pruning**: Optimizes the minimax algorithm by pruning branches that cannot possibly affect the final decision.
- **Optimal Move Selection**: Ensures the best possible move is chosen based on the current game state.

## How it Works

The algorithm performs a depth-first search on the game tree, evaluating the game states by recursively alternating between maximizing and minimizing the player's score. Alpha-beta pruning is applied to eliminate branches of the game tree that don't need to be explored, improving the efficiency of the algorithm.
