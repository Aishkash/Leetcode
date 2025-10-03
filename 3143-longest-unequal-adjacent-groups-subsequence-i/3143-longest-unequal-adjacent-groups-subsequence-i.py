class Solution(object):
    def getLongestSubsequence(self, words, groups):
        if not words:
            return []

        # Start with the first element
        subseq = [words[0]]
        last_group = groups[0]

        # Go through the rest of the elements
        for i in range(1, len(words)):
            if groups[i] != last_group:
                subseq.append(words[i])
                last_group = groups[i]  # update last_group

        return subseq
