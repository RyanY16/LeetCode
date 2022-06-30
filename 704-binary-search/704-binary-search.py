class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowest = 0
        highest = len(nums)-1
        while lowest <= highest:
            middle = (lowest + highest) // 2
            guess = nums[middle]
            if guess == target:
                return middle
            elif guess > target:
                highest = middle - 1
            else: lowest = middle + 1
        return -1