#O(n) time going through each letter | O(1) space for max letters of 26
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        letterCounts = {}

        for i in range(len(word1)):
            letter1 = word1[i]
            letter2 = word2[i]

            if letter1 in letterCounts:
                letterCounts[letter1] += 1
            else:
                letterCounts[letter1] = 1

            if letter2 in letterCounts:
                letterCounts[letter2] -= 1
            else:
                letterCounts[letter2] = -1

        for letter in letterCounts:
            if abs(letterCounts[letter]) > 3:
                return False

        return True
