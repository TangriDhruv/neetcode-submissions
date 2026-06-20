class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix_sum = prefix [i-1] * nums [i-1]
                prefix.append(prefix_sum)
        sufix = []
        nums_rev = nums[::-1]
        for i in range(0,len(nums_rev)):
            if i == 0:
                sufix.append(1)
            else:
                sufix_sum = sufix[i-1] * nums_rev [i-1]
                sufix.append(sufix_sum)
        sufix = sufix[::-1]

        print(sufix)
        print(prefix)
        res = []
        for i in range(0,len(nums)):
            result =prefix[i] * sufix[i]
            res.append(result)
        return res



