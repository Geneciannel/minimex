def show(board):
    # Generate a string for each row and join them with newlines
    rows = [f"  {board[i]} | {board[i+1]} | {board[i+2]}" for i in range(0, 9, 3)]
    print("\n".join(rows))
