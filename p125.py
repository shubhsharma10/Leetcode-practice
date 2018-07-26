class Solution:
    def isPalindrome(self, s):
        permitted = "0123456789abcdefghijklmnopqrstuvwxyz"
        s = s.lower()
        s = "".join(c for c in s if c in permitted)
        return s == s[::-1]