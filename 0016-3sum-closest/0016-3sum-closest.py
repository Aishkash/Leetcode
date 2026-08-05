class Solution(object):
    def threeSumClosest(self, nums, target):
        sz=len(nums)
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        maxxx=float("inf")
        for i in range(sz-2):
            l = i + 1
            r = sz - 1
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                if summ<target:
                    l+=1
                elif summ>target:
                    r-=1
                else:
                    return summ

                diff=abs(summ-target)
                if diff<maxxx:
                    ans=summ
                    maxxx=diff
        return ans
        