class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #combining position and speed array into one using zip
        pair = [[p,s] for p,s in zip(position,speed)]
        stack =[]
        # we are traversing in reverse
        print(pair)
        print(sorted(pair))
        for p,s in sorted(pair)[::-1]:
            #appending the speed
            print((target-p)/s)
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        