class Solution(object):
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - 1
        
        # shrink the window until its size is k
        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
        
        return arr[left:right+1]