class Solution(object):
    def jump(self, nums):
        n = len(nums)
        jumps = 0
        end = 0
        farthest = 0

        for i in range(n - 1):  # we don't need to jump from the last index
            farthest = max(farthest, i + nums[i])
            
            if i == end:  # need to make a jump
                jumps += 1
                end = farthest
        
        return jumps
        
            