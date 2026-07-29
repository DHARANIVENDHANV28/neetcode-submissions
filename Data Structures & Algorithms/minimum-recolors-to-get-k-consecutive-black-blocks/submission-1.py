class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        opr = 0
        output = float("inf")

        for r in range(len(blocks)):
            if blocks[r] == "W":
                opr += 1

            if r - l + 1 > k:
                if blocks[l] == "W":
                    opr -= 1
                l += 1

            if r - l + 1 == k:
                output = min(output, opr)

        return output