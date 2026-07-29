class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        opr = 0
        output = float("+inf")

        for r in range(len(blocks)):
            if r-l == k:
                output = min(output,opr)
                if blocks[l] == "W":
                    opr -= 1
                l += 1

            if blocks[r] == "W":
                opr += 1
            print(blocks[l:r+1],opr)
        output = min(output,opr)
        return output
        