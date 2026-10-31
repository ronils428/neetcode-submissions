class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for s in tokens:
            if s == "+":
                stk.append(stk.pop() + stk.pop())

            elif s == "-":
                num2 = stk.pop()
                num1 = stk.pop()
                stk.append(num1 - num2)

            elif s == "*":
                stk.append(stk.pop() * stk.pop())

            elif s == "/":
                num2 = stk.pop()
                num1 = stk.pop()
                stk.append(int(float(num1) / num2))

            else:
                stk.append(int(s))

        return stk[0]