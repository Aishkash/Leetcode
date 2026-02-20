class Solution(object):
    def majorityElement(self, nums):
        a={}
        sz=len(nums)
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        mid=sz//2
        for i in nums:
            if a[i]>mid:
                return i
        