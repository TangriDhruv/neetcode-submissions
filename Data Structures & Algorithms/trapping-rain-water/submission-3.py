class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        temp_max =0
        for i in range (0, len(height)):
            if i == 0:
                #continue
                #temp_max = 0
                max_left.append(temp_max)
                #print("pos:left",i,max_left)
            else:
                temp_max = max(temp_max,height[i-1])
                max_left.append(temp_max)
                #print("pos:left",i,max_left)
        
        max_right = []
        temp =0
        reverse_height = height[::-1]
        #print(reverse_height)
        for i in range (0, len(reverse_height)):
            if i == 0:
                
                #temp = 0
                max_right.append(temp)
                #print("pos:right",i,max_right)
            else:
                temp = max(temp,reverse_height[i-1])
                max_right.append(temp)
                #print("pos:right",i,max_right)
        res = 0
        reverse_max_right = max_right[::-1]
        for i in range (0, len(height)):
            min_l_r = min(max_left[i],reverse_max_right[i])
            if((min_l_r - height[i])>0):
                res = res + min_l_r - height[i]
            #print("res",res)
        return res



