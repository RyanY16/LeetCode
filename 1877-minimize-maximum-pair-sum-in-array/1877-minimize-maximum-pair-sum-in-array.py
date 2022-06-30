class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        for i in range(int(len(nums)/2)):
            if nums[i] + nums[len(nums)-1-i] > maxSum:
                maxSum = nums[i] + nums[len(nums)-1-i]
        return maxSum
        