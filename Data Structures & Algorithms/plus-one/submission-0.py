class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_digits = len(digits)
        
        for i in range(num_digits - 1, -1, -1):
            if i == (num_digits - 1) or digits[i + 1] == 0:
                digits[i] = (digits[i] + 1) % 10
            if digits[i] > 0:
                break;
        
        if digits[0] == 0:
            digits.insert(0, 1)

        return digits