class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        x = ""
        for i in s:
            if (i.isdecimal() or i.isalpha()):
                x += i
        condition = True
        for i in range(len(x)):
            if (x[i] == x[len(x)-1-i]):
                continue
            condition  = False
            break
        return condition