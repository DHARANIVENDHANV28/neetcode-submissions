class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        hashmap = {}
        for i in range(len(nums2)):
            hashmap[nums2[i]] = -1
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    hashmap[nums2[i]] = nums2[j]
                    break
        
        for n1 in nums1:
            output.append(hashmap[n1])
        return output
                

        