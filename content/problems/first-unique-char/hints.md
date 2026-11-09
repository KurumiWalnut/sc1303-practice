Calling `s.count(c)` for every character is O(N²).

---

The course exercise uses a dict and a queue together. Count each character with the dict, and keep a queue of (character, index) in the order they first appeared. Then drop characters from the front of the queue while their count is more than 1. Two passes over a dict of counts works too.
