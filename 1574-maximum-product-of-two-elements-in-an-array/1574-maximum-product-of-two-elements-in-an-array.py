import heapq
class Solution(object):
    def maxProduct(self, nums):
        nums=[-s for s in nums]
        heapq.heapify(nums)
        a=heapq.heappop(nums)
        b=heapq.heappop(nums)
        a=abs(a)-1
        b=abs(b)-1
        return a*b
        