class Solution(object):
    def threeSum(self, nums):
        # a=[]
        # sz=len(nums)
        # nums.sort()
        # k=sz-1
        # j=1
        # for i in range(sz-2):
        #     k=sz-1
        #     req=(nums[i]+nums[j])*(-1)
        #     while j<k:
        #         if nums[k]==req:
        #             a.append([nums[i], nums[j], nums[k]])
        #             j=i+2
        #             break
        #         elif nums[k]>req:
        #             k-=1
        #         else:
        #             j+=1
        #             break    
        # return a
        triplets = set()
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[k] + nums[j] > -nums[i]:
                    k -= 1
                elif nums[k] + nums[j] == -nums[i]:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                else:
                    j += 1
        return list(triplets)
