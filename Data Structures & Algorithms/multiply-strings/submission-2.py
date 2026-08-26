class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = []
        c = 0
        for n in range(len(num1) + len(num2)):
            p = c
            for t in range(n + 1):
                a_ii = n - t
                b_ii = t

                if a_ii < 0 or b_ii < 0 or a_ii >= len(num1) or b_ii >= len(num2):
                    continue;

                a_i = len(num1) - a_ii - 1
                b_i = len(num2) - b_ii - 1
                

                a_n = int(num1[a_i])
                b_n = int(num2[b_i])

                p += a_n * b_n

            ans.append(str(p % 10))
            c = p // 10

        ans.append(str(c))

        while ans[-1] == "0":
            ans = ans[:-1]

        ans.reverse()
        return "".join(ans)