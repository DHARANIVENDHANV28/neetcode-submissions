class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print("sorted_nums",sorted_nums)
        Output = []
        for idx,i in enumerate(sorted_nums):
            if idx < len(sorted_nums)-2:
                j = idx+1
                k = len(sorted_nums)-1
                print(i,sorted_nums[j],sorted_nums[k])
                while j<k:
                    sum_ = sorted_nums[j]+sorted_nums[k]
                    print(i,sorted_nums[j],sorted_nums[k])
                    if sum_+i > 0:
                        k -= 1
                    if sum_+i < 0:
                        j += 1
                    if sum_+i == 0:
                        Output.append([i,sorted_nums[j],sorted_nums[k]])
                        print("Output",Output)
                        j += 1
        list_1 = []
        for lis in Output:
            if lis not in list_1:
                list_1.append(lis)
        return list_1

        