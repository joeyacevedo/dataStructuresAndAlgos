class Solution: #O(n) time for going through the list and O(n) space for the new array
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        planted = 0

        for i in range(1, len(f) - 1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                planted += 1

        return planted >= n
