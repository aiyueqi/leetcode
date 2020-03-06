from typing import *

class Stack:
    def __init__(self):
        self.stack = [0] * 10000
        self.top = -1
    
    def pop(self):
        if self.top == -1:
            return None
        self.top -= 1

    def push(self, num):
        self.top = self.top + 1
        self.stack[self.top] = num

    def peak(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False
        s = Stack()
        i = 0
        j = 0
        while j < len(popped):
            if s.peak() == None or s.peak() != popped[j]:
                if i == len(pushed):
                    return False
                s.push(pushed[i])
                i += 1
            else:
                s.pop()
                j += 1
        return True

s = Solution()
print(s.validateStackSequences([1,2,3], [3,1,2]))

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        temp = []
        j = 0
        for el in pushed:
            temp.append(el)
            while temp[-1] == popped[j]:
                temp.pop()
                j += 1
                if not temp:
                    break
        return False if temp else True3
