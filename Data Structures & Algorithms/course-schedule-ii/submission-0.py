class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        HashMap = {i:[] for i in range(numCourses)}
        for cour,pre in prerequisites:
            HashMap[cour].append(pre)
        print(HashMap)
        visit, cycle = set(), set()
        output = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for prereq in HashMap[course]:
                if not dfs(prereq): return False 
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course): return []
        return output