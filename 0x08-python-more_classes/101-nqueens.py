#!/usr/bin/python3
"""Solves the N-queens puzzle"""
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


@@ -32,9 +48,11 @@ def get_solution(board):

def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
@@ -83,7 +101,8 @@ def xout(board, row, col):

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens. 
