class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        openers = ['(', '{', '[']
        closers = [')', '}', ']']
        for c in s:
            if c in openers:
                stack.append(c)
            if c in closers:
                if not stack:
                    return False
                i = closers.index(c)
                if openers.index(stack[-1]) == i:
                    stack.pop(-1)
                else:
                    return False
        if not stack:
            return True
        else:
            return False
            

        