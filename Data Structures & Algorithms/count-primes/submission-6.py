class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False]*n
        res = 0
        for num in range(2,n):
            if not sieve[num]:
                res+=1
                for i in range(num*num,n,num):
                    sieve[i] = True
        return res



        # res = 0
        # for num in range(2,n):
        #     isPrime = True
        #     for div in range(2,int(num**0.5)+1):
        #         if num%div == 0:
        #             isPrime = False
        #             break
        #     if isPrime:
        #         res += 1
        # return res