class Solution(object):
    def sortEvenOdd(self, nums):
        evens = sorted(nums[0::2])   
        odds = sorted(nums[1::2], reverse=True) 
        res = []
        
        e = o = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(evens[e])
                e += 1
            else:
                res.append(odds[o])
                o += 1
        return res   
