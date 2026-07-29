class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        output = []

        for n in nums:
            if n<0:
                neg.append(n)
            else:
                pos.append(n)
        
        for i in range(len(pos)):
            output.append(pos[i])
            output.append(neg[i])

        return output

        