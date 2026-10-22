class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 1000000007
        res = 0
        n = len(arr)
        left = [0]*n
        right = [0]*n

        stack = [] 
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            prev = stack[-1] if stack else -1
            left[i] = i-prev
            stack.append(i)

        stack = [] 
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            nxt = stack[-1] if stack else n
            right[i] = nxt-i
            stack.append(i)
        
        for i in range(n):
            res += (arr[i]*left[i]*right[i])
        
        return res%mod
