# 125. Valid Palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            a = s[i]
            b = s[j]
            if a != b:
                return False
            i += 1
            j -= 1

        return True
