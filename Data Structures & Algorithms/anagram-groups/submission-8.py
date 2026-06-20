class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            arr_s =[0]*26
            for i in range(len(s)):
                arr_s[(ord(s[i])-ord("a"))] +=1
            result[tuple(arr_s)].append(s)
        return list(result.values())

        