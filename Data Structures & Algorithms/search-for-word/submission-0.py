delta_positions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows, num_cols = len(board), len(board[0])
        
        used_letter_positions = set()
        used_letters = []

        def visit(i, j):
            if i < 0 or j < 0 or i >= num_rows or j >= num_cols or (i, j) in used_letter_positions:
                return
            used_letters.append(board[i][j])
            used_letter_positions.add((i, j))

            if len(used_letters) == len(word):
                if "".join(used_letters) == word:
                    return True
            else:
                for di, dj in delta_positions:
                    if visit(i + di, j + dj):
                        return True

            used_letters.pop()
            used_letter_positions.remove((i, j))

            return False

        for i in range(num_rows):
            for j in range(num_cols):
                if visit(i, j):
                    return True

        return False

            