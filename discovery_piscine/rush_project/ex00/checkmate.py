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

    # check pawn ข้างล่างซ้าย-ขวา ว่ามี pawn อยู่ไหม
    for column_step in (-1, 1):
        row = king_row + 1
        col = king_col + column_step

        # check ก่อนว่าตำแหน่งไม่เกินขอบตาราง
        if 0 <= row < size and 0 <= col < size:
            if board[row][col] == "P":
                print("Success")
                return

    # direction ทั้งหมดที่ต้องเช็ค
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

    # check ทีละ direction
    for row_step, column_step in directions:
        row = king_row + row_step
        col = king_col + column_step

        # check ทีละ direction ขึ้นไปเรื่อยๆ จนกว่าจะเจอหมาก หรือเกินขอบตาราง
        while 0 <= row < size and 0 <= col < size:
            piece = board[row][col]

            if piece in "PBRQK":
                if row_step == 0 or column_step == 0: # แนวตรง
                    if piece == "R" or piece == "Q":
                        print("Success")
                        return
                else:
                    if piece == "B" or piece == "Q": # แนวทแยง
                        print("Success")
                        return

                break

            row += row_step
            col += column_step

    print("Fail")