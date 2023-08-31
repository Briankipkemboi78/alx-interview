#!/usr/bin/python3
'''solving nqueens problem'''
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen attacking in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, row, N):
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N)
            board[row][col] = 0

def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    solve_nqueens_util(board, 0, N)

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solve_nqueens(N)
