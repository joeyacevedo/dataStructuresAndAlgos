#O(n) time depending on input str | O(n) space most likely because of adding to the stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                kStr = ""
                while stack and stack[-1].isdigit():
                    kStr = stack.pop() + kStr

                stack.append(int(kStr) * substr)

        return "".join(stack)
