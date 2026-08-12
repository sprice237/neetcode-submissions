from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        num_rows = len(grid)
        num_cols = len(grid[0])

        q = deque()

        for y in range(num_rows):
            for x in range(num_cols):
                if grid[y][x] == 0:
                    q.append((x, y, 0))

        deltas = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def bfs():
            x, y, d = q.popleft()

            if not (0 <= x < num_cols and 0 <= y < num_rows):
                return

            if grid[y][x] == -1:
                return

            if d > 0:
                if d < grid[y][x]:
                    grid[y][x] = d
                else:
                    return;

            for dx, dy in deltas:
                q.append((x + dx, y + dy, d + 1))

        while q:
            bfs()



            

