class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current = self.head
        

    def visit(self, url: str) -> None:
        self.current.right = Node(url)
        self.current.right.left = self.current
        self.current = self.current.right

        

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.left:
            steps -= 1
            self.current = self.current.left
        return self.current.val
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.right:
            steps -= 1
            self.current = self.current.right
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)