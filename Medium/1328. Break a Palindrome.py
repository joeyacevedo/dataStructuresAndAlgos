# O(n) time for going through half the palindrome | O(1) space
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''

        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]

        #edge case where all letters are 'a'
        return palindrome[:-1] + 'b'
