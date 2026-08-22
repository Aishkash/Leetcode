class Solution(object):
    def nextGreaterElements(self, nums):
        nums=nums*2
        sz=len(nums)
        stack=[]
        ans=[-1]*sz
        for i in range(sz-1,-1,-1):
            while stack and nums[i]>=stack[-1]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(nums[i])
        return ans[:sz//2]
