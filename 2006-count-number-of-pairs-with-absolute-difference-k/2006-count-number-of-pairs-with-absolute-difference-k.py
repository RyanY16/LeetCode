class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        absoluteDifference = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    absoluteDifference += 1
        return absoluteDifference