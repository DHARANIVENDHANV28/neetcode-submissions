class Solution:
    def countSeniors(self, details: List[str]) -> int:
        output = 0
        for d in details:
            if int(d[11:13]) > 60:
                output += 1
        return output

        