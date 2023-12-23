class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sLetterMap = {}

        for letter in s:
            if letter in sLetterMap:
                sLetterMap[letter] += 1
            else:
                sLetterMap[letter] = 1

        for letter in t:
            if letter in sLetterMap and sLetterMap[letter] >= 1:
                sLetterMap[letter] -= 1
            else:
                return letter

