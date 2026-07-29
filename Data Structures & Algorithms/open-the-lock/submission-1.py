from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1
        
        queue = deque([("0000",0)])
        visited = set(["0000"])

        while queue:
            code,steps = queue.popleft()
            if code == target:
                return steps
            
            for i in range(4):
                digit = int(code[i])
                for move in [-1,1]:
                    new_digit = (digit+move)%10
                    new_code = code[:i]+str(new_digit)+code[i+1:]

                    if new_code not in dead and new_code not in visited:
                        visited.add(new_code)
                        queue.append((new_code,steps+1))
        return -1