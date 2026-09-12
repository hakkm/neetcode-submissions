import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall(r"[A-Za-z0-9]+", s)).lower()
        for left in range(len(s)//2):
            right = len(s) - left - 1 
            if s[left] != s[right]:
                return False
        return True
