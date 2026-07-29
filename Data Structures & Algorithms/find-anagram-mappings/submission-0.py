class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        HashMap = {}
        for idx,n2 in enumerate(nums2):
                HashMap[n2] = idx
        
        mapping = []
        for n1 in nums1:
            mapping.append(HashMap[n1])
        
        return mapping

        