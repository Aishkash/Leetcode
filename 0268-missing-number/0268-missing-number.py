class Solution(object):
    def missingNumber(self, nums):
        sz=len(nums)
        k=0
        a=sum(nums)
        for i in range(1,sz+1):
            k+=i
        return k-a
