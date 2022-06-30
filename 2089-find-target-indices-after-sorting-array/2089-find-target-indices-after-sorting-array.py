class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        array = []
        for i in range(len(nums)):
            if target == nums[i]:
                array.append(i)
        return array