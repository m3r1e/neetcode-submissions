class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()])
        s=s.lower()
        l = 1
        r = 1
        while l+r<=len(s):
            if s[l-1] == s[-r]:
                l+=1
                r+=1
            else:
                return False
        return True
