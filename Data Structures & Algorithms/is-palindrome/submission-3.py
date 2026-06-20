class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_str = ""
        for char in s:
            print(char)
            if char.isalnum():
                print(char)
                final_str = final_str+char.lower()
                print(final_str)
        if final_str == final_str[::-1]:
            return True
        return False
        