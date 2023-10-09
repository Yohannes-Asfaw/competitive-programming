def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            digits[i], rem = (digits[i] + 1) % 10, (digits[i] + 1) // 10
            if not rem: return digits
        return [rem]+digits
