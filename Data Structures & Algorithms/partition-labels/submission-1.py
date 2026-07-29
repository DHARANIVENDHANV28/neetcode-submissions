class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        HashMap = {}
        for idx,c in enumerate(s):
            HashMap[c] = idx
        output = []
        end = 0
        size = 0
        for i,c in enumerate(s):
            size += 1
            end = max(end,HashMap[c])
            if i == end:
                output.append(size)
                size = 0
        return output




        # seen = set()
        # output = []
        # out = 0
        # HashMap = {}
        # for c in s:
        #     if c not in HashMap:
        #         HashMap[c] = 1
        #     else:
        #         HashMap[c] += 1

        # for i in s:
        #     if HashMap[i]:
        #         HashMap[i] -= 1
        #         seen.add(i)
        #     if not HashMap[i]:
        #         seen.remove(i)
        #     out += 1
        #     if not seen:
        #         output.append(out)
        #         out = 0
        # return output

        