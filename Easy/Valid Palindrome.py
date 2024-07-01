# Problem 125 - Valid Palindrome
# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        s = s.lower()

        for c in s:
            if c.isalnum():
                new_s += c
        
        return new_s == new_s[::-1]
        