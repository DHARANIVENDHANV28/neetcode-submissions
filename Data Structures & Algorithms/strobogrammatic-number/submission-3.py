class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        HashMap = { "0":"0",
                    "1":"1",
                    "6":"9",
                    "8":"8",
                    "9":"6"
                    }

        num1 = list(num)[::-1]
        for i,n in enumerate(num1):
            if n in HashMap:
                num1[i] = HashMap[n]
            else:
                return False
        
        return num == "".join(num1)
        