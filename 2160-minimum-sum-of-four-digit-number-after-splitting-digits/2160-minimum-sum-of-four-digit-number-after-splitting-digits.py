class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        array = [num[0], num[1], num[2], num[3]]
        array.sort()
        return 10*(int(array[0])+int(array[1])) + int(array[2]) + int(array[3])