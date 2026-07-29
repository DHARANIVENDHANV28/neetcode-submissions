class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HashMap = {}
        for val in nums:
            if val not in HashMap:
                HashMap[val] = 1
            else:
                HashMap[val] = HashMap[val] + 1
        Output = []
        # print(HashMap)
        sorted_by_values = dict(sorted(HashMap.items(),reverse=True, key=lambda item: item[1]))
        print("sorted_by_values",sorted_by_values)
        cnt = 0
        for key,val in sorted_by_values.items():
            cnt += 1
            print(sorted_by_values[key])
            if cnt <= k:
                Output.append(key)
        return Output

        
        # HashMap_ = {val:key for key,val in HashMap.items()}
        # print(HashMap_)
        
        # decending_order = sorted(HashMap_.keys(),reverse = True)
        # print(decending_order)

        # for iter_,ele in enumerate(decending_order):
        #     print('iter',iter_)
        #     if iter_ < k:
        #         Output.append(HashMap_[ele]) 
        # return Output



        