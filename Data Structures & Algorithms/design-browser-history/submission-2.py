class Node:
    def __init__(self,val="",next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        newnode=Node(url)
        self.cur.next = newnode
        newnode.prev=self.cur
        self.cur=newnode

    def back(self, steps: int) -> str:
        while self.cur:
            if steps == 0 or not self.cur.prev: #or not self.cur.prev for 1 node
                return self.cur.val
            steps-=1
            self.cur=self.cur.prev
    """
    why self.cur.prev in condition: 
    google(only node)
    ↑ cur

    without it: 
    back(5)
    while self.cur → True (cur=google)
    steps=5, 5!=0
    steps=4
    self.cur = self.cur.prev = None   ← cur is now None
    while None → exits loop
    no return hit → returns None  

    correct:
    while self.cur → True (cur=google)
    steps=5, not self.cur.prev → True  ← check BEFORE moving
    return self.cur.val = google ✅
    """
    def forward(self, steps: int) -> str:
        while self.cur:
            if steps == 0 or not self.cur.next: 
                return self.cur.val
            steps-=1
            self.cur=self.cur.next

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)