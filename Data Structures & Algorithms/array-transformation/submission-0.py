class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        # ar = [0]*len(arr)
        opr = True
        if len(arr) <=2:
            return arr

        while opr==True:
            ar = [0]*len(arr)
            ar[0] = arr[0]
            opr = False
            for i in range(1,len(arr)-1):
                if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                    ar[i] = arr[i]-1
                    opr = True
                elif arr[i]<arr[i-1] and arr[i]<arr[i+1]:
                    ar[i] = arr[i]+1
                    opr = True
                else:
                    ar[i] = arr[i]

            ar[-1] = arr[-1]
            arr = ar
        return arr
            


        