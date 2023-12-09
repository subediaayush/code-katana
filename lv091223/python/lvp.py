class Solution:
    def longestValidParentheses(self, s) -> int:
        # stack = []
        # lvp = 0
        # currentVP = 0
        # while(len(s) > 0):
        #     inp = s[0]
        #     s = s[1:]
        #     if (inp == '('):
        #         stack.append(inp)
        #     else:
        #         if len(stack) == 0:
        #             if currentVP > lvp:
        #                 lvp = currentVP

        #             currentVP = 0
        #             continue
        #         stack.pop()    
        #     currentVP += 1
        
        # return max(lvp, currentVP) - len(stack)
        if len(s) == 0: return -1

        start = s[0]
        vp = 0
        if (start == '('):
            lvp = self.longestValidParentheses(s[1:])
            if (lvp != -1): vp += lvp
            return vp
        else:
            return 2

print(Solution().longestValidParentheses('((())'))