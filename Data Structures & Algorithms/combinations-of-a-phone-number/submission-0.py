class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def f(word):
            if not word:
                return []

            c, rest = word[0], word[1:]
        
            letters = d[c]
            rest_options = f(rest) if len(rest) > 0 else [""]
            combined = []

            for l in letters:
                for o in rest_options:
                    combined.append(l + o)
                    
            return combined

        return f(digits)