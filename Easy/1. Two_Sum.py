class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsHashMap = {}

        for idx in range(len(nums)):
            remainder = target - nums[idx]
            if remainder in numsHashMap:
                return [idx, numsHashMap[remainder]]
            else:
                numsHashMap[nums[idx]] = idx
