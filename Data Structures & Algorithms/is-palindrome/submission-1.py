class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = s.split(" ")
        string = ""
        for word in words:
            string = string + word.lower()
        string_clean = re.sub(r'[^\w\s]', '', string)
        palindrome = string_clean[::-1]
        
        print(string_clean)
        print(palindrome)

        if (string_clean == palindrome):
            return True

        return False
        