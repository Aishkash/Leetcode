class Solution(object):
    def majorityElement(self, nums):
        sz=len(nums)//2
        k={}
        for i in nums:
            if i not in k:
                k[i]=1
            else:
                k[i]+=1

        for i in nums:
            if k[i]>sz:
                return i
        