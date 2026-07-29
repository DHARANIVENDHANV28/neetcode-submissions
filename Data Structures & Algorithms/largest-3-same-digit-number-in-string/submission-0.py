class Solution:
    def largestGoodInteger(self, num: str) -> str:

        res = float("-inf")

        for i in range(0,len(num)-2):
            NUM = int(num[i:i+3])
            if len(set(num[i:i+3])) == 1:
                print(NUM)
                res = max(res,NUM)
        if res == 0:
            return "000"
        elif res < 0:
            return ""
        else:
            return str(res) 

        