class Solution(object):
    def twoSum(self, numbers, target):
        a=[]
        sz=len(numbers)
        i,j=0,sz-1
        while i<j:
            summ=numbers[i]+numbers[j]
            if summ>target:
                j-=1
            elif summ<target:
                i+=1
            else:
                a.append(i+1)
                a.append(j+1)
                return a
