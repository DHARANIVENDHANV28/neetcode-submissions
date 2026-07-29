class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        HashMap = {1:0,0:0}

        for s in students:
            if s not in HashMap:
                HashMap[s] = 0
            HashMap[s] += 1
        print(HashMap)
        
        for s in sandwiches:
            print(HashMap)
            if HashMap[s] > 0:
                res -= 1
                HashMap[s] -= 1
            else:
                return res
        return res