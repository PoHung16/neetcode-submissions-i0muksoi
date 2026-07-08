"""
 OOD: Yes
 Constraints: Yes
 input : Implement constructor and method
 output : Implement constructor and method
"""
#A.Clarify the goal : Design a stack class that supports the push, pop, top, and getMin operations.
#B.Design the data structure : 
    # main stack : save all elements
    # min stack: save the current minimum.  Min stack will always have minimum on top , and can be fetched in O(1)
#C.Implement constructor and method
    # getMin should run in O(1) time.

# Keyword : “MinStack in O(1) time" -> Two Stacks
# Approach :Sync a min-stack to to track the minimum value at every step  with the main stack to track all elements

class MinStack:
    def __init__(self):
        self.main_stack = [] # track all elements
        self.min_stack = [] # track the minimum value at every step .  Min stack will always have minimum on top , and can be fetched in O(1)
    def push(self, val:int)->None:
        self.main_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            currentMin = self.min_stack[-1]
            if val < currentMin:
                self.min_stack.append(val)
            else:
                self.min_stack.append(currentMin) # self.min_stack top stay the same #為了同步2個stack長度
    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()
    def top(self)->int:
        return self.main_stack[-1]
    def getMin(self)->int:
        return self.min_stack[-1]


# Time complexity: O(1) 
# Space complexity:  O(N)....create 2 size N Stack

def test():
    minstack = MinStack()
    minstack.push(1)
    minstack.push(2)
    minstack.push(0)
    minstack.getMin()
    minstack.pop()
    top = minstack.top()
    minimum = minstack.getMin()
    print(f"Top: {top} , Minimum: {minimum}") #return 2, 1

if __name__ == "__main__":
    test()
