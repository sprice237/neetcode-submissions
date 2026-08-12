from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in seen:
                    continue

                if grid[i][j] == "0":
                    seen.add((i, j))
                    continue

                q = deque([(i, j)])
                def bfs():
                    i, j = q.popleft()

                    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or (i, j) in seen:
                        return

                    seen.add((i, j))

                    if grid[i][j] == "0":
                        return

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        q.append((i + dx, j + dy))

                while q:
                    bfs()
                
                num_islands += 1

        return num_islands