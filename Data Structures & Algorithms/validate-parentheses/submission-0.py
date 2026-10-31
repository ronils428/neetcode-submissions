class Solution:
    def isValid(self, s: str) -> bool:
        # dict of opening and closing pairs
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # empty stack
        stk = []

        # one pass - O(n)
        for char in s:

            # if value is closing parentheses
            if char in pairs:

                # check if stack has items and the item below is it's pair
                if stk and stk[-1] == pairs[char]:
                    stk.pop()
                else:
                    return False
                    
            # otherwise add the element to the stack
            else:
                stk.append(char)

        if not stk:
            return True
        else:
            return False