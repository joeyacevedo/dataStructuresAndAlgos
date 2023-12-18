class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumOfNums = sum(nums)
        leftSum = 0

        for idx, num in enumerate(nums):
            if leftSum == (sumOfNums - leftSum - num):
                return idx
            leftSum += num

        return -1
