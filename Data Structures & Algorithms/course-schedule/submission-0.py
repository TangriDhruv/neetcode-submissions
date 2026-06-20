class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i:[] for i in range(numCourses)}
        

        for crs,prereq in prerequisites:
            pre_map[crs].append(prereq)
        print(pre_map)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if pre_map[course] == []:
                return True
            
            visited.add(course)
            print("****",visited)
            for pre in pre_map[course]:
                print("pre: ",pre)
                if not dfs(pre):
                    return False
            print("###",course)
            visited.remove(course)
            pre_map[course] = []
            return True
        
        for crs in range(numCourses):
            print("crs",crs)
            if not dfs(crs):
                return False
        
        return True
        