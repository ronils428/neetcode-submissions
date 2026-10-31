class MinStack:

    def __init__(self):
        # init two stacks - one for operation, one for min
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # add val to stack
        self.stack.append(val)

        # if minStack, get the minimum between added value and what's already in minStack
        if self.minStack:
            val = min(val, self.minStack[-1])

        # store min in minStack
        self.minStack.append(val)

    def pop(self) -> None:
        # pop from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
