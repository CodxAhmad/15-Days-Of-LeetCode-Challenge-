class Solution(object):
    def lengthOfLastWord(self, s):
        lis = s.split()
        print(lis)
        return len(lis[-1])