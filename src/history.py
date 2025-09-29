
class BrowserHistory:
    def __init__(self, start="home"):
        self._cur = start
        self._back = []
        self._fwd = []
        self._started = False

    def visit(self, url: str) -> None:
        if self._started:
            self._back.append(self._cur)
        self._cur = url
        self._fwd.clear()
        self._started = True

    def back(self) -> str:
        if not self._back:
            raise IndexError("No more pages in back history")
        self._fwd.append(self._cur)
        self._cur = self._back.pop()
        return self._cur

    def forward(self) -> str:
        if not self._fwd:
            raise IndexError("No more pages in forward history")
        self._back.append(self._cur)
        self._cur = self._fwd.pop()
        return self._cur

    def current(self) -> str:
        return self._cur


