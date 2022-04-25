class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        palstr = xstr[::-1]
        if xstr == palstr:
            return("true")