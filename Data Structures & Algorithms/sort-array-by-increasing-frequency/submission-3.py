class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        output = [[]]*len(nums)
        res = []
        HashMap = {}
        for n in nums:
            if n not in HashMap:
                HashMap[n] = 0
            HashMap[n] += 1
        for k,v in HashMap.items():
            if len(output[v-1]) == 0:
                output[v-1] = [k]
            else:
                output[v-1] += [k]
                output[v-1]=sorted(output[v-1],reverse = True)
        for idx in range(len(output)):
            if output[idx] != []:
                for n in range(len(output[idx])):
                    for _ in range(idx+1):
                            res.append(output[idx][n])
        return res

        