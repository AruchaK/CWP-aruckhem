def checkmate(board):
    board = board.splitlines()
    print(board)
    if not any(row.strip() for row in board):
        print("Error: no board provided")
        return

    size = len(board)

    if any(len(row) != size for row in board):
        print("Error: board is not square")
        return

    king = None

    for row in range(size):
        for col in range(size):
            if board[row][col] == "K":
                if king is not None:
                    print("Error: multiple kings found")
                    return
                king = (row, col)

    if king is None:
        print("Error: no king found")
        return

    king_row, king_col = king

    # Pawn check
    for dc in (-1, 1):
        row = king_row + 1
        col = king_col + dc

        if 0 <= row < size and 0 <= col < size:
            if board[row][col] == "P":
                print("Success")
                return

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in directions:
        row = king_row + dr
        col = king_col + dc

        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]

            if piece in "PBRQK":
                if dr == 0 or dc == 0:
                    if piece == "R" or piece == "Q":
                        print("Success")
                        return
                else:
                    if piece == "B" or piece == "Q":
                        print("Success")
                        return

                break

            row += dr
            col += dc

    print("Fail")