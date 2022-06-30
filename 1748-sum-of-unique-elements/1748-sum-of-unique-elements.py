class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        array = []
        duplicates = []
        for i in nums:
            if i not in array:
                array.append(i)
            elif i not in duplicates:
                duplicates.append(i)
        return sum(array) - sum(duplicates)
        