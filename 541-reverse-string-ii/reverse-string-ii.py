class Solution(object):
    def reverseStr(self, s, k):
        lis = []
        for i in range(0, len(s)+1, 2*k):
            lis.append(s[i:i + k][::-1])
            lis.append(s[i + k:i + 2 * k])
        return ''.join(lis)