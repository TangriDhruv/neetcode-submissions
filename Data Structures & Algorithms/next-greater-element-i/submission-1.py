class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        for index,num in enumerate(nums1):
            mapping[num] = index
        res = [-1]*len(nums1)
        stack = []
        for num in nums2:
            
            while stack and num > stack[-1]:
                curr = stack.pop()
                index = mapping[curr]
                res[index] = num

            if num in mapping:
                stack.append(num)
        return res

