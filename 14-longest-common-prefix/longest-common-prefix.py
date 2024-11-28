class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for string in strs:
                if string[i] != shortest[i]:
                    return shortest[:i]  
        return shortest