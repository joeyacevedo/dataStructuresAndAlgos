import collections

#O(n) space and O(nlogn) for sorting
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        countHash = collections.Counter(arr)
        sortedList = sorted(countHash.values())

        while k > 0:
            if sortedList[0] == 1:
                del sortedList[0]
            else:
                sortedList[0] -= 1
            k -= 1

        return len(sortedList)
