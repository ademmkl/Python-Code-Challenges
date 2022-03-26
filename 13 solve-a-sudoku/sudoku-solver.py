puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def sudokuSolver(rows):

    for y in range(0, 9):
        for x in range(0, 9):
            if rows[y][x] == 0:
                for i in range(1, 10):
                    allowed = True
                    for j in range(0, 9):
                        if (rows[y][j] == i) or (rows[j][x] == i):
                            allowed = False
                    for k in range(0, 3):
                        for z in range(0, 3):
                            if rows[y - y % 3 + k][x - x % 3 + z] == i:
                                allowed = False
                    if allowed:
                        rows[y][x] = i
                        if trial := sudokuSolver(rows):
                            return trial
                        else:
                            rows[y][x] = 0
                return False
    return rows


print(sudokuSolver(puzzle))
