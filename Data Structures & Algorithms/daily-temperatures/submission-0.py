class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        a = [0 for _ in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            while s and s[-1][0] < t:
                s_t, s_i = s.pop()
                a[s_i] = i - s_i
                
            s.append((t, i))

        return a
            