class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupeHash = {}

        for element in nums:
            if element in dupeHash:
                dupeHash[element] += 1
            else:
                dupeHash[element] = 1

        for element in nums:
            if dupeHash[element] >= 2:
                return True

        return False
