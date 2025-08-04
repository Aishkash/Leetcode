import heapq
class Solution(object):
    def largestInteger(self, num):
        digits = list(map(int, str(num)))

        even_heap=[]
        odd_heap=[]

        for i in digits:
            if i%2==0:
                heapq.heappush(even_heap, -i)
            else:
                heapq.heappush(odd_heap, -i)

        result=[]
        for i in digits:
            if i%2==0:
                result.append(-heapq.heappop(even_heap))
            else:
                result.append(-heapq.heappop(odd_heap))

        return int(''.join(map(str, result)))