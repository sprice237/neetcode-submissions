class Solution:
    def climbStairs(self, n: int) -> int:
        solutions = {}
        
        def i(steps: int) -> int:
            if steps < 0:
                return 0
            if steps == 0:
                return 1

            if steps in solutions:
                return solutions[steps]

            s = i(steps - 1) + i(steps - 2)

            solutions[steps] = s

            return s

        return i(n)