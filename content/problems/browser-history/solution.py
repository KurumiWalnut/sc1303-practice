class Page:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage):
        self.current = Page(homepage)

    def visit(self, url):
        page = Page(url)
        page.prev = self.current
        self.current.next = page        # drops the old forward history
        self.current = page

    def back(self, steps):
        while steps > 0 and self.current.prev is not None:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps):
        while steps > 0 and self.current.next is not None:
            self.current = self.current.next
            steps -= 1
        return self.current.url
