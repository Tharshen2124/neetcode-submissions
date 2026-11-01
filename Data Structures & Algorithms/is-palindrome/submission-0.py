import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s  = s.lower()
        mod_s = re.sub(r'[^a-zA-Z0-9]', '', lower_s)

        for i in range(int(len(mod_s)/ 2)):
            if mod_s[i] != mod_s[len(mod_s) - i - 1]:
                return False

        return True

        