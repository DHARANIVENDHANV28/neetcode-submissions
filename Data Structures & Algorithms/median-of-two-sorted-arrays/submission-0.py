class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_arr = []
        i,j = 0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] <= nums2[j]:
                sorted_arr.append(nums1[i])
                i+=1
            else:
                sorted_arr.append(nums2[j])
                j+=1
        while i<len(nums1):
            sorted_arr.append(nums1[i])
            i+=1
        while j<len(nums2):
            sorted_arr.append(nums2[j])
            j+=1
        l = 0
        r = len(sorted_arr)-1
        m = (l+r)//2
        if len(sorted_arr)%2 == 0: #even
            median = (sorted_arr[m]+sorted_arr[m+1])/2
        else:
            median = sorted_arr[m]
        return median

            
        
        