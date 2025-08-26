from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        freq = Counter(s)
        
        # Sort characters by frequency (descending)
        sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
        
        # Build the result string
        result = ''.join([char * count for char, count in sorted_chars])
        return result