class Solution:
    def isPalindrome(self, x: int) -> bool:
    # Write your code here.
        string = str(x)
        return string == string[::-1]
