class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.minstack:             
            return None
        return self.minstack[-1]
        #brute force
        #return min(self.stack)
        


"""
keep a miminum stack, of same size actual stack. 
when pushed at current state of stack its min is stored.
when popped current min is also popped


optimal:
time:
getMin : o(1) with minstack
directly finding min is o(n)

space:
"""