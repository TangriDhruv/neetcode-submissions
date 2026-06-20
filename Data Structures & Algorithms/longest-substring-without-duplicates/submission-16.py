class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = {}
        l = 0
        max_string = 1
        for i,letter in enumerate(s):
            if letter in seen and seen[letter]>=l:
                l = seen[letter] + 1
                
            seen[letter] = i
            max_string = max(max_string,i-l+1)

        return max_string


        