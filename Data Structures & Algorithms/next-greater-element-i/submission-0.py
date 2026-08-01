class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []

        for i in range(0,len(nums1)):
            print(nums1[i])
            j = nums2.index(nums1[i])
            print("j:", j)
            for k in range(j+1,len(nums2)):
                print("k: ",k)
                print("nums2[k]: ",nums2[k])
                if nums2[k] > nums1[i]:
                    print("here")
                    res.append(nums2[k])
                    print(res)
                    break
            else:
                res.append(-1)
        return res