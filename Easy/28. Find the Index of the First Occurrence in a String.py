# Time - Big O(n*m) iterating through length of haystack and needle
# Space - Big O(1) if you do two nested for loops
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i

        return -1
