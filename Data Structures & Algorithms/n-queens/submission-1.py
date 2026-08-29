class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        size = n
        board = [[False] * size for _ in range(size)]

        solutions = []

        def add_board_to_solutions():
            nonlocal board
            nonlocal solutions

            solution = ["".join(["Q" if cell else "." for cell in row]) for row in board]
            print(solution)

            solutions.append(solution)

        # keyed by j
        cols = set()

        # keyed by i - j
        pos_diag = set()

        # keyed by i + j
        neg_diag = set()

        def walk():
            nonlocal n
            nonlocal size
            nonlocal cols
            nonlocal pos_diag
            nonlocal neg_diag

            i = size - n
            
            for j in range(size):
                if j in cols or (i - j) in pos_diag or (i + j) in neg_diag:
                    continue
                
                board[i][j] = True
                cols.add(j)
                pos_diag.add(i - j)
                neg_diag.add(i + j)
                n -= 1

                if n == 0:
                    add_board_to_solutions()
                else:
                    walk()

                board[i][j] = False
                cols.remove(j)
                pos_diag.remove(i - j)
                neg_diag.remove(i + j)
                n += 1

        walk()

        return solutions