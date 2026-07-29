class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = list(set(nums))
        Output = [[i]for i in nums_set if i-1 not in nums_set]
        for st in Output:
            next_num = st[-1]+1
            while next_num in nums_set:
                st.append(next_num)
                next_num += 1
        return max([len(l) for l in Output]) if len(Output) != 0 else 0
          

        
        