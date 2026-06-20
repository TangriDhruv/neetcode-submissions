class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)
        while(l<r):
            print("here")
            for i in range (l+1,r):
                if(numbers[l]+numbers[i] == target):
                    print("i", i, numbers[i])
                    print("l", l, numbers[l])
                    return [l+1,i+1]
            l = l+1
        return []

        