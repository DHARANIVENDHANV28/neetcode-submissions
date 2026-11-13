class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        # n = len(s)
        # res = 0

        # for l in range(n):
        #     count = [0]*10
        #     for r in range(l,n):
        #         digit = int(s[r])
        #         count[digit]+=1
        #         freq = [x for x in count if x>0]
        #         if len(set(freq))==1:
        #             res+=1
        # return res

        n = len(s)
        res = set()

        for l in range(n):
            count = [0] * 10

            for r in range(l, n):
                digit = int(s[r])
                count[digit] += 1

                # Collect frequencies of distinct digits
                freq = [c for c in count if c > 0]

                # All frequencies must be equal
                if len(set(freq)) == 1:
                    res.add(s[l:r+1])

        return len(res)