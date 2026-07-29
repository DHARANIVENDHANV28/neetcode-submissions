class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {p:speed[i] for i,p in enumerate(position)}
        S_position = sorted(position)[::-1]
        stack = []
        for p in S_position:
            num = (target-p)/hashmap[p]
            if stack and stack[-1]>=num:
                continue
            stack.append(num)
        return len(stack)
            
       
        