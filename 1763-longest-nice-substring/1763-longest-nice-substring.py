class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dfs(string):
            hashset = set(string)
            if len(string) < 2:
                return ""
            for i in range(len(string)):
                if not (string[i].lower() in hashset and string[i].upper() in hashset):
                    str1 = dfs(string[:i])
                    str2 = dfs(string[i+1:])
                    return str2 if len(str2) > len(str1) else str1
            return string
        return dfs(s)
                
                
                
                    
                    
        