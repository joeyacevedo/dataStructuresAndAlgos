#O(n) time and space
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', ']':'[', '}':'{'}
        tup = ('(', '[', '{')
        openToClose = set(tup)

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            elif c in openToClose:
                stack.append(c)

        return True if not stack else False
