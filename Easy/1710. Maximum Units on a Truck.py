# O(n) time for going through n boxes | O(1) space
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        unitCount = 0

        for box in boxTypes:
            #destructuring
            numberOfBoxes, unitsPerBox = box

            if numberOfBoxes <= truckSize:
                unitCount += (numberOfBoxes * unitsPerBox)
                truckSize -= numberOfBoxes
            else:
                #using truckSize as it's the remaining number of boxes that fit
                unitCount += (truckSize * unitsPerBox)
                truckSize = 0

            if truckSize == 0: break

        return unitCount
