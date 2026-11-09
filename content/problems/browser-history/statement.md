Build the back/forward history of a browser tab.

- `BrowserHistory(homepage)` starts on `homepage`.
- `visit(url)` goes to `url` and **clears all forward history**.
- `back(steps)` moves back up to `steps` pages (it can't go past the first page) and returns the current URL.
- `forward(steps)` moves forward up to `steps` pages and returns the current URL.

### Example

```text
h = BrowserHistory("leetcode.com")
h.visit("google.com"); h.visit("facebook.com"); h.visit("youtube.com")
h.back(1)      →  "facebook.com"
h.back(1)      →  "google.com"
h.forward(1)   →  "facebook.com"
h.visit("linkedin.com")          # forward history is gone
h.forward(2)   →  "linkedin.com"
h.back(2)      →  "google.com"
h.back(7)      →  "leetcode.com"
```

### Constraints

- Up to 100 000 calls in total, so each call should take O(steps) time or better.
