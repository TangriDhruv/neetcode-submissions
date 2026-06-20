class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]
        
        while len(stones)>1:
            stones.sort()

            first_stone = stones.pop()
            second_stone = stones.pop()

            if first_stone == second_stone:
                stones.append(0)
            else:
                stones.append(first_stone-second_stone)
            
        return stones[0]

        