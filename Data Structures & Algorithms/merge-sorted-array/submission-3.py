class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0
        while nums1 and nums1[-1] == 0:
            nums1.pop()
        while nums1 and i < len(nums1) and j < n:
            if (nums1[i] > nums2[j]):
                nums1.insert(i,nums2[j])
                # nums1.pop()
                print(nums1)
                j+=1
                i+=1                
            else:
                i+=1
        nums1.extend(nums2[j:])
        
            
