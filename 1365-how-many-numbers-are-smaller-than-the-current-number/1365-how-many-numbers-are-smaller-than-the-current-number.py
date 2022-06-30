class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        array = []
        for i in nums:
            noSmaller = 0
            for j in nums:
                if i > j:
                    noSmaller += 1
            array.append(noSmaller)
        return array