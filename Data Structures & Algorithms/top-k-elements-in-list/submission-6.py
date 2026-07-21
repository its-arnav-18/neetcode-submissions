class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b=[]
        for x in Counter(nums).most_common(k):
            b.append(x[0])
        return b
        