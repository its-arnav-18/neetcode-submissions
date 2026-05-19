from functools import reduce
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for ops in operations:
            if ops =="+":
                score.append(score[-1]+score[-2])
            elif ops == "D":
                score.append(2*score[-1])
            elif ops == "C":
                score.pop()
            else:
                score.append(int(ops))
        return sum(score)