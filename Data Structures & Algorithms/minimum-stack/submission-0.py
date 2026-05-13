"""
 OOD: Yes
 Constraints: No
 input : String
 output : boolean
"""
#A.Clarify the goal : Design a stack class that supports the push, pop, top, and getMin operations.
#B.Design the data structure : 
    # data_stack : save all elements
    # Auxiliary stack: save the current minimum.
    # when we push new element, compare new element with Auxiliary stack top, push the smaller element into Auxiliary stack
    # Then auxiliary stack top will always have minum on top , and can be fetched in O(1)
#C.Implement constructor and method
    # getMin should run in O(1) time.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val:int)->None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_minimum = self.min_stack[-1]
            if val < current_minimum: 
                self.min_stack.append(val)
            else:
                self.min_stack.append(current_minimum)
    def pop(self)->None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    def top(self)->int:
        return self.stack[-1]
    def getMin(self)->int:
        return self.min_stack[-1]

def test():
    minstack = MinStack()
    minstack.push(1)
    minstack.push(2)
    minstack.push(0)
    minstack.pop()
    top = minstack.top()
    minimum = minstack.getMin()
    print(f"Top: {top} , Minimum: {minimum}")


if __name__ == "__main__":
    test()

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create 2 size N Stack