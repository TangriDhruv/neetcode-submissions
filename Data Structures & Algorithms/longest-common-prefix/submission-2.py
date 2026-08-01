class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = ""
        curr_shortest_len = float("inf")
        for s in strs:
            if len(s) < curr_shortest_len:
                curr_shortest_len = len(s)
                shortest_word = s
        #print(shortest_word)

        for s in strs:
            #print(s)
            for i in range (0, len(shortest_word)):
                #print(i)
                if  shortest_word[i] != s[i]:
                    shortest_word = shortest_word[:i]
                    break
                #print("short: ",shortest_word )
        return shortest_word 



            
        