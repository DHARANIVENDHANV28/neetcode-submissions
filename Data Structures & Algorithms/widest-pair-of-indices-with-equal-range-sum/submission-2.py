class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        prefix = 0
        res = 0
        HashMap = {0:-1}

        for i in range(len(nums1)):
            prefix += nums1[i]-nums2[i]
            if prefix in HashMap:
                res = max(res,i-HashMap[prefix])
            else:
                HashMap[prefix] = i
        return res
        