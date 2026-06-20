class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26 #create a list of 26 zeros cause 26 alphabests and 
            for c in s:
                count[ord(c) -ord('a')] += 1 # one hot encoding (adding one where you find the character)
            res[tuple(count)].append(s) # appending for same key
        return list(res.values()) # return list 