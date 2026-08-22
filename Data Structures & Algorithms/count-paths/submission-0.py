class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}

        def count_paths(i, j):
            try:
                return mem[(i, j)]
            except KeyError:
                pass

            if i >= m or j >= n:
                mem[(i, j)] = 0
                return 0
            
            if i == m - 1 and j == n - 1:
                mem[(i, j)] = 1
                return 1

            res = count_paths(i + 1, j) + count_paths(i, j + 1)
            mem[(i, j)] = res

            return res

        return count_paths(0, 0)