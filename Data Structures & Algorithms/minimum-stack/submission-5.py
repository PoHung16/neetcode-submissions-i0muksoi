"""
 OOD: Yes
 Constraints: Yes
 input : Implement constructor and method
 output : Implement constructor and method
"""
#A.Clarify the goal : Design a stack class that supports the push, pop, top, and getMin operations.
#B.Design the data structure : 
    # main stack : save all elements
    # min stack: save the current minimum at each step.  Min stack will always have minimum on top , and can be fetched in O(1). Min stack size should always sync with main stack size
#C.Implement constructor and method
    # getMin should run in O(1) time.

# Keyword : getMin in O(1) time" -> Two Stacks
# Approach :Sync a min-stack to to track the minimum value at every step  with the main stack to track all elements

class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
    def push(self, val:int):
        self.main_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            currentMin = self.min_stack[-1]
            if val < currentMin:
                self.min_stack.append(val)
            else:
                self.min_stack.append(currentMin)
    def pop(self):
        self.main_stack.pop()
        self.min_stack.pop()
    def top(self):
        return self.main_stack[-1]
    def getMin(self):
        return self.min_stack[-1]

# Time complexity: O(1) 
# Space complexity:  O(N)....create 2 size N Stack

def test():
    minstack = MinStack()
    minstack.push(1)
    minstack.push(2)
    minstack.push(0)
    getmin_value = minstack.getMin()
    top_value = minstack.top()
    minstack.pop()
    getmin_second_value = minstack.getMin()
    print(f"Top: {top_value} , Minimum: {getmin_value} and {getmin_second_value}") #return 2, 1

if __name__ == "__main__":
    test()
