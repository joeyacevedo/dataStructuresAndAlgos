class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}

        for char in s:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1

        for idx in range(len(s)):
            if hashMap[s[idx]] == 1:
                return idx
        return -1
