class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        HashMap = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            HashMap[course].append(prereq)
        print(HashMap)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if HashMap[course] == []:
                return True
            visited.add(course)
            for prereq in HashMap[course]:
                if not dfs(prereq): return False
            visited.remove(course)
            HashMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True
        