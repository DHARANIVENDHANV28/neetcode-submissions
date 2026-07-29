class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ws = len(s1)
        for i in range(len(s2)):
            sliced = s2[i:i+ws]
            if sorted(s1) == sorted(sliced):
                return True
        return False
        