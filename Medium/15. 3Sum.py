class Solution: #O(n^2) because of the nested loops, space would be O(n) for the python sorting algo
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        #should I modify the array or copy before sorting?
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    answer.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return answer
