class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = 1 , 10000
        while right >= left:
            mid = (left + right) // 2
           
            if Solution.sol(weights,mid,days) == True:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def sol(weights,mid,days):
        collect = []
        counter = 0
        res = []
        i = 0
        while i < len(weights):
           
            if sum(collect) + weights[i] <= mid:
                collect.append(weights[i])
                
                res.append(weights[i])
                i += 1
            elif collect:
                counter += 1
                
                collect = []
            else:
                return False
                

        if collect and collect[-1] == weights[-1]:
            counter +=1
     
        if counter <= days and res == weights:
            return True

        else:
            return False
