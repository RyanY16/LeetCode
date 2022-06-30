class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        array = []
        for i in sentence:
            if i not in array:
                array.append(i)
        if len(array) == 26:
            return True
        else: return False
        