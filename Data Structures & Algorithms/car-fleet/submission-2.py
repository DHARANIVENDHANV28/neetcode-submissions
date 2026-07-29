class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        fleet = 0
        max_time = 0
        cars.sort(reverse=True)

        for p,s in cars:
            t = (target-p)/s
            if t>max_time:
                fleet+=1
                max_time = t
        return fleet
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # hashmap = {p:speed[i] for i,p in enumerate(position)}
        # S_position = sorted(position)[::-1]
        # stack = []
        # for p in S_position:
        #     num = (target-p)/hashmap[p]
        #     if stack and stack[-1]>=num:
        #         continue
        #     stack.append(num)
        # return len(stack)
            
       
        