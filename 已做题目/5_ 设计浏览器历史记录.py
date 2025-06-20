class BrowserHistory:

    def __init__(self, homepage: str):
        self.prev = None
        self.next = None
        self.name = homepage
        self.curr = self

    def visit(self, url: str) -> None:
        url = BrowserHistory(url)
        self.curr.next = url
        url.prev = self.curr
        self.curr = url

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
            else:
                break
        return self.curr.name

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                break
        return self.curr.name


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# https://leetcode.cn/problems/design-browser-history/