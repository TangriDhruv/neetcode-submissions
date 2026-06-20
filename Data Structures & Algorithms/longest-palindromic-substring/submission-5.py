class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        store = defaultdict()
        for i in range(0,len(s)):
            sub_string = s[i]
            store[sub_string] = len(sub_string)
            for r in range(i+1,len(s)):
                sub_string = sub_string + s[r]
                if sub_string == sub_string[::-1]:
                    store[sub_string] = len(sub_string)
        
        store = [(k,v) for k,v in sorted(store.items(), key=lambda item: item[1],reverse = True)]
        print(store)
        
        return store[0][0]
        