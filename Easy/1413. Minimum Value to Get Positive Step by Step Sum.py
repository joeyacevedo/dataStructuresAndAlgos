# O(n) time for looping through nums | O(1) space
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        maxDifference = 0
        runningSum = 0

        for num in nums:
            runningSum +=  num
            if runningSum < maxDifference: maxDifference = runningSum

        return abs(maxDifference) + 1

