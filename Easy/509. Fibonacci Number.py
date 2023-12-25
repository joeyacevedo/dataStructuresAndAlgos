class Solution:
    memo = {}

    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        if n-1 not in self.memo: self.memo[n-1] = self.fib(n-1)
        if n-2 not in self.memo: self.memo[n-2] = self.fib(n-2)

        return self.memo[n-1] + self.memo[n-2]
