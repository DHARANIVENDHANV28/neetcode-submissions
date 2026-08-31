class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l = 0
        r = 0
        i = 0

        while r<n and l<=r:
            while r<n and chars[l]==chars[r]:
                r+=1
            cnt = r-l
            chars[i] = chars[l]
            if cnt != 1:
                for c in str(cnt):
                    i+=1
                    chars[i] = c
            i+=1

            l = r
        return i

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(chars)
        # i,k = 0,0

        # while i<n:
        #     chars[k] = chars[i]
        #     k+=1
        #     j = i+1
        #     while j<n and chars[i]==chars[j]:
        #         j+=1
        #     if j-i > 1:
        #         for c in str(j-i):
        #             chars[k] = c
        #             k+=1
        #     i = j
        # return k
        
        