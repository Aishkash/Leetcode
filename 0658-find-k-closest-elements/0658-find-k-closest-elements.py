import heapq

class Solution(object):
    def findClosestElements(self, arr, k, x):
        # max-heap with negative distance
        heap = []
        
        for num in arr:
            # push (negative distance, negative num) to break ties in favor of smaller numbers
            heapq.heappush(heap, (-abs(num - x), -num))
            if len(heap) > k:
                heapq.heappop(heap)  # remove farthest
        
        # extract numbers from heap and sort them
        result = [-num for (_, num) in heap]
        result.sort()
        return result