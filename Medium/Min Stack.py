# Problem 155 - Min Stack
# https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.min) > 0:
            if val <= self.min[-1]:
                self.min.append(val)
        else:
            self.min.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]