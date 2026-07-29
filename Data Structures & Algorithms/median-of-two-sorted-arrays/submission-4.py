class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        total = len(A)+len(B)
        half = total//2

        if len(A)>len(B):
            A,B=B,A

        la = 0
        ra = len(A)-1

        while True:
            ma = (la+ra)//2
            mb = half-ma-2
            Al = A[ma] if ma>=0 else float("-infinity")
            Ar =  A[ma+1] if (ma+1)<len(A) else float("infinity")
            Bl = B[mb] if mb >=0 else float("-infinity")
            Br = B[mb+1] if (mb+1)<len(B) else float("infinity")

            if Al<=Br and Bl<=Ar:
                if total%2==0:
                    return (max(Bl,Al)+min(Br,Ar))/2
                else:
                    return min(Ar,Br)
            elif Al>Br:
                ra = ma-1
            else:
                la = ma+1

       
        # sorted_arr = []
        # i,j = 0,0
        # while i<len(nums1) and j<len(nums2): #O(m+n)
        #     if nums1[i] <= nums2[j]:
        #         sorted_arr.append(nums1[i])
        #         i+=1
        #     else:
        #         sorted_arr.append(nums2[j])
        #         j+=1
        # while i<len(nums1): #O(n)
        #     sorted_arr.append(nums1[i])
        #     i+=1
        # while j<len(nums2): #O(m)
        #     sorted_arr.append(nums2[j])
        #     j+=1
        # l = 0
        # r = len(sorted_arr)-1
        # m = (l+r)//2
        # if len(sorted_arr)%2 == 0: #even
        #     median = (sorted_arr[m]+sorted_arr[m+1])/2
        # else:
        #     median = sorted_arr[m]
        # return median

            
        
        