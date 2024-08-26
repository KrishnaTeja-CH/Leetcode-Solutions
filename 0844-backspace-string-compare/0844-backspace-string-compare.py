class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(string):
            stack = []
            for i in string:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            return stack
        return backspace(s) == backspace(t)
                


        