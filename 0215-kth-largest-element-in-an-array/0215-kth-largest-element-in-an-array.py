import heapq
class Solution(object):
    def findKthLargest(self, nums, k):

        lums=[-s for s in nums]
        heapq.heapify(lums)
        # pq=[]
        while k>0:
            if k==1:
                t=heapq.heappop(lums)
            else:
                heapq.heappop(lums)
            k-=1   
        t=t*(-1)     
        if t in nums:
            return t
        return abs(t)  

        
        