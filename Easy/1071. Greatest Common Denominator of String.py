class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l or len2 % l:
                return False
            factor1, factor2 = len1 // l, len2 // l
            if str1[:l] * factor1 == str1 and str2[:l] * factor2 == str2:
                return True

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]

        return ""
