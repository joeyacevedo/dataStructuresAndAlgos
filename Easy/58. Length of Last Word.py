class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleanString = s.strip()
        splitString = cleanString.split()

        return len(splitString[-1])
