class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        d = {}

        def dfs(a):
            if a < 0:
                return -1
            if a == 0:
                return 0

            if a in d:
                return d[a]
                
            dfs_results = [dfs(a - c) for c in coins]
            valid_dfs_results = [x for x in dfs_results if x >= 0]

            d[a] = 1 + min(valid_dfs_results) if valid_dfs_results else -1

            return d[a]



        return dfs(amount)