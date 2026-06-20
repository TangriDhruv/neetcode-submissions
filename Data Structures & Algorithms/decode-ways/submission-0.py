class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(index):
            # If we've reached the end, that means we've formed a valid decoding
            if index == len(s):
                return 1
            
            # A leading zero cannot be decoded
            if s[index] == '0':
                return 0
            
            # Option 1: Decode single digit
            ways = dfs(index + 1)

            # Option 2: Decode two digits (if valid)
            if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
                ways += dfs(index + 2)
            
            return ways
        
        return dfs(0)


        