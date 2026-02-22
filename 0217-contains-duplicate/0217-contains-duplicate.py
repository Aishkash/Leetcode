class Solution(object):
    def containsDuplicate(self, nums):
        k=set()
        for num in nums:
            if num not in k:
                k.add(num)
            else:
                return True
        return False
        