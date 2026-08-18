class Solution(object):
    def findDisappearedNumbers(self, nums):
        sz=len(nums)
        a=[]
        for i in nums:
            if nums[abs(i)-1]>0:
                nums[abs(i)-1]*=-1
        for i in range(sz):
            if nums[i] >0:
                a.append(i+1)
        return a