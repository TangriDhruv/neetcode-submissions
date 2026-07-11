class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_str = ""
        for i in s:
            if i.isalnum():
                final_str = final_str + i.lower()
        if final_str == final_str[::-1]:
            return True
        return False
        