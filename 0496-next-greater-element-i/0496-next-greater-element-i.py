class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        sz=len(nums2)
        ans={}
        stack=[]
        ans2=[]
        for i in range(sz-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()
            if len(stack)==0:
                ans[nums2[i]]=-1
            else:
                ans[nums2[i]]=stack[-1]
            
            stack.append(nums2[i])
        
        for i in nums1:
            ans2.append(ans[i])

        return ans2