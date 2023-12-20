class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry, index = 1, 0

        while carry:
            if index < len(digits):
                if digits[index] == 9:
                    digits[index] = 0
                else:
                    digits[index] += 1
                    carry = 0

            else:
                digits.append(carry)
                carry = 0
            index += 1

        return digits[::-1]
