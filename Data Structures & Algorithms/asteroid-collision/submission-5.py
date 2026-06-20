class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # process collisions
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < -a:       # stack asteroid explodes
                    stack.pop()
                    continue
                elif stack[-1] == -a:    # both explode
                    stack.pop()
                break                     # new asteroid is destroyed
            
            else:
                stack.append(a)
        
        return stack
