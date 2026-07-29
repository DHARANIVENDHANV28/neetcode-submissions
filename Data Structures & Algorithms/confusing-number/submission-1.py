class Solution:
    def confusingNumber(self, n: int) -> bool:
        HashMap = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        n_ = list(str(n))
        for idx,num in enumerate(n_):
            if num not in HashMap:
                return False
            n_[idx] = HashMap[num]
        print(n_)
        
        return False if int("".join(n_[::-1])) ==  n else True