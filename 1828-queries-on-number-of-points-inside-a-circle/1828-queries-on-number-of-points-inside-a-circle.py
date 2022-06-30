class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for i in queries:
            count = 0
            for j in points:
                if (i[0]-j[0])**2 + (i[1]-j[1])**2 <= i[2]**2:
                    count += 1
            answer.append(count)
        return answer