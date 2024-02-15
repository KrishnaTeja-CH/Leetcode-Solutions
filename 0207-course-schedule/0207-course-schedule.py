class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
         
        pre = defaultdict(list)
        for course, p in prerequisites:
            pre[course].append(p)
    
        taken = set()               # We are taking set to see there is no circle                 
        
        def dfs(course):            # Create A dfs with the course, and add courses.
            
            if not pre[course]:     # If pre req of that course is empty we can complete the course.
                return True
            
            if course in taken:     # if course already taken, doesnt work
                return False
                
            taken.add(course)       # Add courses, that are not taken     
            
           
            for p in pre[course]:   # Now check each pre-requsisite of that course
                if not dfs(p):
                    return False
                
                                    # If all cases are satisfied, upodate the list
            
            pre[course] = []        # Now we can complete this course, and this is dfs
            return True
                                    # Now we are calling the dfs from outside
            
        for course in range(numCourses):
            if not dfs(course):
                return False        # We are calling dfs to confirm, there is no circle
        
        return True                 # If everything qualifies, return True
        
        