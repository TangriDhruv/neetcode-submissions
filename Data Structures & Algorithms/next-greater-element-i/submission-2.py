class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        for index,num in enumerate(nums1):
            mapping[num] = index
        stack = []
        res = [-1] * len(nums1)
        for i in range(0,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                curr = stack.pop()
                res[mapping[curr]] = nums2[i]
                
            if nums2[i] in mapping:
                stack.append(nums2[i])
        return res


        